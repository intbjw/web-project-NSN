import time
import datetime
import urllib.parse
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
        isrisk = self.sifting()
        if isrisk:
            flag = self.isDirBusetr()
        else:
            self.risk_level = 0
    def isDirBusetr(self):
        #用户可能不止发动了一次攻击,因此对于单纯的判断404的比例是不靠谱的
        #判断策略：设置一个阈值，如500 如果短时间超过500次404
        #或者大于100且不足500，但是404的比重占到了百分之70以上
        #对于小于100次的请求 不认为存在目录爆破行为
        #对于短时间的定义：这里先制定一个阈值为频率2秒一次
        #注意一些特殊的user-agent
        count = 0
        time = self.logs[0].date.getSec()
        for log in self.logs:
            if WebDate.sec_minutes(time,log.date.getSec())<2 and log.status_code == 404:
                count += 1
            time = log.date.getSec()
        if count > 500 or count >= 0.7*len(self.logs):
            return True
        else:
            return False
    def sifting(self):
        black_agent = ("ZmEu","Baiduspider","python-requests")
        sql_inject = ("select","/**/","or","#","--","and","union","from","where")
        xss_inject = ("script","javascript","alert","href","<a","src","var","Image")
        shell_inject = ("chmod","curl","sh","wget")
        #注意大小写
        #在对url进行解析的时候比较复杂 需要url进行解码
        #制定关于威胁排除的规则
        #若用户连接数小于200 访问不包含敏感目录 无常见的shell
        #user-agent正常
        #无xss SQL等关键字，则视为无危胁
        #"GET /bWAPP/htmli_get.php?firstname=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&lastname=%3Ca+
        #href%3D%22http%3A%2F%2Flocalhost%22%3E%3C%2Fa%3E&form=submit
        if len(self.logs) >= 200:
                return True
        for log in self.logs:
            #处理异常user-agent
            if log.user_agent == "-" or log.user_agent in black_agent:
                return True
            #url解析 然后处理各种注入
            url = urllib.parse.unquote(log.header.split[1]).lower()
            for i in sql_inject:
                if i in url:
                    return True
            for i in shell_inject:
                if i in url:
                    return True
            for i in xss_inject:
                if i in xss_inject:
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