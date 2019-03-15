# -*- coding: UTF-8 -*-
import time
import datetime
import urllib.parse
import re
from urllib.parse import urlparse
from urllib.parse import quote,unquote
import json
from html import unescape
import base64
#用于解析web目录的一个类
class Log():
    '''
    该类用于表示一个web日志，其包含一个日志的各种属性
    '''
    def __init__(self,s):
        self.sourcelog = s
        self.parseWebLog(s)
    
    def parseWebLog(self,s):
        #按照双引号来分割字符串
        s = s.split('"')
        #得到IP和访问日期
        self.ip = s[0].split()[0]
        #日期设计成一个类
        self.date = WebDate(s[0].split()[-2][1:])
        #得到未被进一步分割的首部字段
        #不要提前url解码和分割，有些参数带空格的，影响解析
        self.header = s[1]
        #得到状态码和数据长度
        self.status_code = int(s[2].split()[0])
        try:
            #对于一些没有数据的长度 将其长度归零，比如head请求
            self.length = int(s[2].split()[1])
        except ValueError:
            self.length = 0
        #得到用户提出请求时所在的URL和user-agent
        try:
            self.url = s[3]
            self.user_agent = self.parseUserAgent(s[5])
        except:
            self.url = '-'
            self.user_agent = '未记录'
    def parseUserAgent(self,s):
        
        patterns ={ r"Mozilla/\d[.]\d [(].+?[)] AppleWebKit/\d{1,5}[.]\d{1,5} [(].+?[)] Chrome/.*? Safari/\d{1,5}[.]\d{1,5}":"Chrome",
                    r"python-requests/\d[.]\d{1,2}[.]\d":"python-requests",
                    r"Mozilla/\d[.]\d [(].+?[)] AppleWebKit/\d{1,5}[.]\d{1,5}[.]\d{1,3} [(].+?[)] Version/.*? Safari/\d{1,5}[.]\d{1,5}[.]\d{1,3}":"Safari(Mac os)",
                    r"Mozilla/\d[.]\d [(]iPhone;.*?[)] AppleWebKit/\d{1,5}[.]\d{1,5}[.]\d{1,3}":"Safari(iPhone)",
                    r"Mozilla/\d[.]\d [(].+?[)] Gecko/\d+ [ 0-9a-zA-Z.()/]*Firefox":"Firefox",
                    r"RPS/HTTP PROXY":"RPS",
                    r"WordPress/\d{1,3}[.]\d{1,3}[.]\d{1,3};":"WordPress",
                    r"Apache":"Apache",
                    r"Mozilla/\d.\d [(]compatible[:;] MSIE \d{1,2}[.]\d; Windows NT \d{1,2}[.]\d":"IE",
        }
        for i in patterns.keys():
            compile = re.compile(i)
            if compile.search(s):
                return patterns[i]
        return "Unknow type("+s+")"

class WebDate():
    #29/Jan/2019:06:28:10
    def __init__(self,date):
        self.raw_date = date
        self.__second = self.timesec(date)
    def getSec(self):
        return self.__second
    @staticmethod
    def timesec(date):
        monthdic = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
                    "Jul":7,"Aug":8,"Sec":9,"Oct":10,"Nov":11,"Dec":12                    
                }
        monthday = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        date = date.split("/")
        day = int(date[0])
        month = monthdic[date[1]]
        #处理年，时分秒
        date = date[2].split(":")
        year = int(date[0])
        hour = int(date[1])
        minute = int(date[2])
        sec = int(date[3])
        
        all_day = day
        if year%400==0 or (year%4==0 and year%100!=0):
            monthday[2] = 29
        else:
            monthday[2] = 28 
        for i in range(1,month):
            all_day += monthday[i]
        if datetime.datetime(year,month,day).strftime("%w") == '0':
            week = 6
        else:
            week = int(datetime.datetime(year,month,day).strftime("%w"))-1
        all_sec = int(time.mktime((year,month,day,hour,minute,sec,week,all_day,0)))
        return all_sec
    #所有的时间统一按照秒来计算
    def sec_obj_minutes(self,s):
        #求两个时间对象的时间差
        return abs(self.__second - s.getSec())
    @staticmethod
    def sec_minutes(sec1,sec2):
        #求两个秒的差
        return abs(sec1-sec2)

class WebRisk():
    #传过来的参数实际上是一个以相同IP为单位的log对象列表
    #该类比较关键 设计安全威胁评级 一定要于图形界面好好的对应
    #该类功能尚未实现完整
    def __init__(self,logs):
        self.logs = logs
        self.risk_level = 0
        self.black_agent = ("ZmEu","Baiduspider","python-requests")
        self.sql_inject = ("select"," ","#","--","and","union","from","where","insert","update")
        self.shell_inject = ("chmod","curl","sh","wget")
        self.date = logs[0].date.raw_date
        self.risktype = ""
        self.riskdescribe = ""
        self.ip = logs[0].ip
        self.ipcount = len(logs)
        self.user_agent = logs[0].user_agent
        self.DirBusetr_num = 0
        self.CmdExecute_num = 0
        self.PasswdBuster_num = 0
        self.SqlInjection_num = 0
        self.FileInclude_num = 0
        self.Xss_num = 0
        isrisk = self.sifting()
        if isrisk:
            #除文件爆破之外 似乎所有的判断对于post都是无效的
            #漏洞威胁分4个等级，4是最高级,存在多种漏洞取最高级
            #优化了顺序  防止低级覆盖高级
            if self.isDirBusetr():
                self.risk_level = 1
                self.risktype += "目录爆破,"
                self.riskdescribe += "网站后台目录存在被爆破风险."
                self.DirBusetr_num = self.DirBusetr_num + 1
            if self.isXss():
                self.risk_level = 2
                self.risktype += "xss攻击,"
                self.riskdescribe += "疑似遭到XSS攻击."
                self.Xss_num = self.Xss_num + 1
            if self.isPasswdBuster():
                self.risk_level = 3
                self.risktype += "口令猜解,"
                self.riskdescribe += "疑似后台有恶意爆破密码行为."
                self.PasswdBuster_num = self.PasswdBuster_num + 1
            if self.isSqlInjection():
                self.risk_level = 4
                self.risktype += "SQL注入,"
                self.riskdescribe += "疑似发现SQL注入行为."
                self.SqlInjection_num = self.SqlInjection_num + 1
            if self.isCmdExecute():
                self.risk_level = 4
                self.risktype += "命令执行,"
                self.riskdescribe += "疑似被执行恶意命令."
                self.CmdExecute_num = self.CmdExecute_num + 1
            if self.isfileinclude():
                self.risk_level = 4
                self.risktype += "文件包含,"
                self.riskdescribe += "疑似请求中包含文件."
                self.FileInclude_num = self.FileInclude_num + 1
            self.risktype = self.risktype[:-1]

    def isDirBusetr(self):
        '''
        该函数用于判断是否存在目录爆破威胁，其判断思路为：计算用户短时间内请求状态码
        404出现数量，大于阈值，即可确定。为防止用户不止进行了一种攻击的情况出现导致
        该方法失效，基于攻击时扫描占大多数这一情况，辅助判断为若404占比达到70%
        且访问路径数量达到20，即认为存在该威胁。若用户访问量很小，但是请求头疑似爬虫，
        也视为威胁。
        (曾遇到一种密码爆破情况，因事先删除了文件，所以状态全是404，但仅访问一个文件,
        因此对访问路径数量也设置了限制
        )
        '''
        count = 0
        path_set = set()
        isspider = False
        time = self.logs[0].date.getSec()
        for log in self.logs:
            #将所有出现的资源添加到一个集合中
            try:
                path_set.add(urllib.parse.urlparse(unquote(log.header.split()[1])).path)
            except:
                pass
            #如果存在2秒内进行一次请求
            if WebDate.sec_minutes(time,log.date.getSec())<5 and log.status_code == 404:
                count += 1
            for i in self.black_agent:
                if log.user_agent == "-" or i in log.user_agent:
                    isspider = True
            time = log.date.getSec()
        #短时间资源不存在的情况达到300次 或者虽未达到300 但70%及以上的访问均无效
        #在大量的访问下，若访问路径数大于阈值，可以确定存在目录爆破行为
        if (count > 300 or count >= 0.7*len(self.logs)) and len(path_set)>20:
            return True
        #20%以上的访问均无效,且请求头异常,疑似爬虫 或者,访问的资源位置
        elif count>0.2 and isspider:
            return True
        else:
            return False
    def isSqlInjection(self):
        #正则和关键字检查互相辅助
        raw_str = [r"select [0-9a-z_$,]+ from [0-9a-z_$]+",
        r"'.*or''=",r"'.*or [0-9a-z]*(=| =| = )[0-9a-z]*",
        r"or .*? (--|#)"
        ]
        for log in self.logs:
            try:
                query = unquote(log.header.split()[1]).lower()
            except:
                query = '-'
            #将查询字符串中的连接符转换为空格
            query = query.replace("+"," ")
            query = query.replace("/**/"," ")
            '''
            for i in self.sql_inject:
                if i in query:
                    return True
            '''
            
        for i in raw_str:
            match = re.search(i,query)
            if match:
                return True
        return False
    def isXss(self):
        for log in self.logs:
            #先将url解析出来，然后将+号等特殊符号转换为空格
            try:
                #先转化为小写
                url = unquote(log.header.split()[1]).lower().replace("+"," ")
                #将实体字符转化为普通字符
                url = unescape(url)
                #如果采用的字符集利用了base64
                if url.find('base64,') != -1:
                    tpattern = r'base64,.*"'
                    tmatch = re.search(tpattern,url)
                    if tmatch:
                        urltmp = tmatch.group()[7:-1]
                        url = url.replace(urltmp,base64.b64decode(urltmp).decode())
            except:
                url = '-'
            patterns = [
                r"<script>.*</script>",
                r"alert[(].*?[)]",
                r"<a .*?=.*?>.*?</a>",
                r'''body onload="alert('.*?')"[><]{0,2}[/]{0,1}body''',
                r'iframe.*/iframe'

            ]
            for pattern in patterns:
                compile = re.compile(pattern)
                match = compile.search(url)
                if match:
                    return True
        return False
    def isPasswdBuster(self):
        '''
        该方法用于确定访问中是否存在口令猜解行为
        口令可能出现在post方法中，也可能出现在get方法中
        但是无论何种方法，都会访问登陆页面，因此只需关注登录页面即可
        口令猜解危害较大，若疑似猜解次数达到20，即视为威胁
        '''
        #此目录为登录页面目录，可以借助文件读取进来，登录界面的目录可由用户提供
        #测试阶段暂时定为一个已知的列表
        pwd_dir = ["login.php","admin.php","xmlrpc.php"]
        count = 0
        time = self.logs[0].date.getSec()
        for log in self.logs:
            try:
                url = unquote(log.header.split()[1]).lower()
            except:
                url = '-'
            if log.date.sec_minutes(time,log.date.getSec()) < 20:
                url = urllib.parse.urlparse(url).path
                for i in pwd_dir:
                    if i in url:
                        count += 1
                if count == 20:
                    break
            time = log.date.getSec()
        if count >= 20:
            return True
        else:
            return False


    def isCmdExecute(self):
        #初期不具有判断是否攻击成功的功能
        '''
        判断命令执行漏洞的策略：检查是否存在一些常见的危险的命令
        只要存在威胁的命令即认为有问题
        为增加判断的准确性，这里将利用正则表达式进行匹配
        第一版的函数只对一些常见的参数进行正则匹配和关键字查找
        '''
        raw_str = [r"chmod ([+]x|[0-9a-z]{3}) [a-z0-9_]+[.][a-z0-9]+",
                    r"wget http[/0-9a-z_&=]+",r"(sh|bash) .+[.]sh",
                    r'system[(]".+"[)]'
            ]
        blackkey = ("shell_exec","passthru","popen","proc_popenla","phpinfo()")
        for log in self.logs:
            try:
                url = unquote(log.header.split()[1]).lower()
            except:
                url = '-'
            for i in blackkey:
                if i in url:
                    return True
            for i in raw_str:
                pattern = re.compile(i)
                match = pattern.search(url)
                if match:
                    return True
        return False
    def isfileinclude(self):
        '''
        实现思路
        检测URL中传递的参数
        如果传递的参数是一个文件的话 则视为文件包含
        '''
        patterns = [
            r".*[.]txt",
            r".*[.]php",
            r".*[.]conf",
            r".*[.]log",
            r".*[.]xml"
        ]
        for log in self.logs:
            try:
                url = unquote(log.header.split()[1]).lower()
            except:
                url = '-'
            params_pos = url.find('?')
            params = url[params_pos:].split('&')
            for param in params:
                #得到了很多的参数 其中包括可能存在的文件地址参数
                try:
                    p = param.split("=")[1]
                    for i in patterns:
                        #已经是小写了，好像忽略大小写没啥必要加了
                        match = re.search(i,p,re.IGNORECASE)
                        if match:
                            return True
                except:
                    pass
        return False
    def sifting(self):
        '''
        该类用于初步判断某IP的请求是可能否存在威胁
        若请求较多(暂定200)，认为可能存在威胁
        若请求较少，粗略的根据user-agent，和一些SQL语句等判断
        存在威胁的可能
        '''
        #注意大小写 注意对URL编码的请求进行解码
        xss_inject = ("script","javascript","alert","href","<a","src","var","Image")
        if len(self.logs) >= 200:
                return True
        for log in self.logs:
            #处理异常user-agent
            if log.user_agent == "-" or log.user_agent in self.black_agent:
                return True
            #url解析 然后处理各种注入
            try:
                url = unquote(log.header.split()[1]).lower()
            except:
                url = '-'
            for i in self.sql_inject:
                if i in url:
                    return True
            for i in self.shell_inject:
                if i in url:
                    return True
            for i in xss_inject:
                if i in xss_inject:
                    return True
            if self.isPasswdBuster():#数据量少的情况下直接对口令猜解进行一次完整测试
                return True
        return False

def parseIp(logs):
    #先遍得到所有IP，然后分类
    iplist = []
    ipdic = {}
    ipset = set()
    #首先拿到所有IP地址
    for log in logs:
        ipset.add(log.ip)
    #将对应地址的log对象列表置空
    for ip in ipset:
        ipdic[ip] = []
    #遍历log对象，并根据IP将其添加到合适的列表中
    for log in logs:
        ipdic[log.ip].append(log)
    #将列表从字典中提取出来
    for k in ipdic.keys():
        if len(ipdic[k]) > 2:
            iplist.append(ipdic[k])
    return iplist
def makejson(risk_lists):
    #传递的参数是一个webrisk对象的列表
    js_result = []
    for risk in risk_lists:
        #如果存在威胁的话
        if risk.risk_level != 0 and risk.ip != '127.0.0.1':
            dic = {}
            dic["ip"] = risk.ip
            dic["date"] = risk.date
            dic["user-agent"] = risk.user_agent
            dic["level"] = risk.risk_level
            dic["describe"] = risk.riskdescribe
            dic["type"] = risk.risktype
            dic['ipcount'] = risk.ipcount
            js_result.append(dic)
    js_str = json.dumps(js_result)
    with open("data.json","w") as f:
        f.write(js_str)

class Statistics():
    '''
    该类用于统计数据
    1.访问次数最高的前10个IP
    2.访问次数最高的前10个URL
    3.攻击次数统计
    '''
    def CountIP(self,logs):
        IPset = {}
        for log in logs:
            IPset[log.ip] = IPset.get(log.ip,0) + 1
        IPset = sorted(IPset.items(),key=lambda x:x[1],reverse = True)
        return IPset[:10]

    def CountURL(self,logs):
        URLset = {}
        for log in logs:
            try:
                url = unquote(log.header.split()[1])
                o = urlparse(url)
                URLset[o[2]] = URLset.get(o[2],0) + 1
            except IndexError:
                pass
        URLset = sorted(URLset.items(), key=lambda x: x[1], reverse=True)
        return URLset[:10]

    def CountAttack(self,Attack):
        Attackset = {}
        Attackset['目录爆破'] = Attackset.get('目录爆破',0) + Attack[0]
        Attackset['命令执行'] = Attackset.get('命令执行', 0) + Attack[1]
        Attackset['口令猜解'] = Attackset.get('口令猜解', 0) + Attack[2]
        Attackset['SQL注入'] = Attackset.get('SQL注入', 0) + Attack[3]
        Attackset['xss攻击'] = Attackset.get('xss攻击', 0) + Attack[4]
        '''
        临时加进来的一个 注意不要越界
        到时候在把文件包含加进来吧
        '''
        #暂时改好了 修改了analyse.py中数组元素的个数 增添了统计时关于文件包含的统计
        #并且 图表成功的自动拓展了
        Attackset['文件包含'] = Attackset.get('文件包含',0) + Attack[5]
        Attackset = sorted(Attackset.items(), key=lambda x: x[1], reverse=True)
        return Attackset