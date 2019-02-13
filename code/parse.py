import time
import datetime
import urllib.parse
import re
#用于解析web目录的一个类
#webRisk类尚有很多欠缺的地方  需要进行补充
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
        #email和用户名字这里不再获取
        #得到未被进一步分割的首部字段
        self.header = s[1]
        #得到状态码和数据长度
        self.status_code = int(s[2].split()[0])
        try:
            #对于一些没有数据的长度 将其长度归零，比如head请求
            self.length = int(s[2].split()[1])
        except ValueError:
            self.length = 0
        #得到用户提出请求时所在的URL和user-agent
        self.url = s[3]
        self.user_agent = s[5]
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
        self.sql_inject = ("select","/**/","or","#","--","and","union","from","where")
        self.xss_inject = ("script","javascript","alert","href","<a","src","var","Image")
        self.shell_inject = ("chmod","curl","sh","wget")
        isrisk = self.sifting()
        if isrisk:
            #除文件爆破之外 似乎所有的判断对于post都是无效的
            #评级标准有待制定
            if self.isDirBusetr():
                self.risk_level = 1
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
            path_set.add(urllib.parse.urlparse(log.header.split()[1]).path)
            #如果存在2秒内进行一次请求
            if WebDate.sec_minutes(time,log.date.getSec())<2 and log.status_code == 404:
                count += 1
            for i in self.black_agent:
                if log.user_agent == "-" or i in log.user_agent:
                    isspider = True
            time = log.date.getSec()
        #短时间资源不存在的情况达到500次 或者虽未达到500 但70%及以上的访问均无效
        #在大量的访问下，若访问路径数大于阈值，可以确定存在目录爆破行为
        if (count > 500 or count >= 0.7*len(self.logs)) and len(path_set)>20:
            return True
        #30%以上的访问均无效,且请求头异常,疑似爬虫 或者,访问的资源位置
        elif count>0.3 and isspider:
            return True
        else:
            return False
    def isSqlInjection(self):
        #建议利用一下正则匹配进行完善 第一版先进行简单的处理
        for log in self.logs:
            url = urllib.parse.unquote(log.header.split()[1]).lower()
            for i in self.sql_inject:
                if i in url:
                    return True
        return False
    def isXss(self):
        for log in self.logs:
            url = urllib.parse.unquote(log.header.split()[1]).lower()
            for i in self.xss_inject:
                if i in url:
                    return True
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
            url = urllib.parse.unquote(log.header.split()[1]).lower()
            if log.date.sec_minutes(time,log.date.getSec()) < 2:
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

<<<<<<< HEAD
    def isCmdExecute(self):    
        for log in self.logs:
            url = urllib.parse.unquote(log.header.split()[1]).lower()
            for i in self.shell_inject:
                if i in url:
                    return True
=======

    def isCmdExecute(self):
>>>>>>> 64c97aae2bbe033477d506ec4fda5da97eecd59f
        #初期不具有判断是否攻击成功的功能
        '''
        判断命令执行漏洞的策略：检查是否存在一些常见的危险的命令
        只要存在威胁的命令即认为有问题
        为增加判断的准确性，这里将利用正则表达式进行匹配
        '''
        raw_str = [r"chmod ([+]x|[0-9a-z]{3}) [a-z0-9_]+[.][a-z0-9]+",
                    r"wget http[/0-9a-z_&=]+",r"(sh|bash) .+[.]sh"
            ]
        blackkey = ("shell_exec","passthru","popen","proc_popenla")
        for log in self.logs:
            url = urllib.parse.unquote(log.header.split()[1]).lower
            for i in blackkey:
                if i in url:
                    return True
            for i in raw_str:
                pattern = re.compile(i)
                match = pattern.search(url)
                if match:
                    return True
        return False
            #
    def sifting(self):
        '''
        该类用于初步判断某IP的请求是可能否存在威胁
        若请求较多(暂定200)，认为可能存在威胁
        若请求较少，粗略的根据user-agent，和一些SQL语句等判断
        存在威胁的可能
        '''
        #注意大小写 注意对URL编码的请求进行解码
        
        if len(self.logs) >= 200:
                return True
        for log in self.logs:
            #处理异常user-agent
            if log.user_agent == "-" or log.user_agent in self.black_agent:
                return True
            #url解析 然后处理各种注入
            url = urllib.parse.unquote(log.header.split[1]).lower()
            for i in self.sql_inject:
                if i in url:
                    return True
            for i in self.shell_inject:
                if i in url:
                    return True
            for i in self.xss_inject:
                if i in self.xss_inject:
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
        iplist.append(ipdic[k])
    return iplist