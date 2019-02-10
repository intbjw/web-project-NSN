#用于解析web目录的一个类
import time
import datetime
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
        return abs(self.__second - s.second)
    @staticmethod
    def sec_minutes(sec1,sec2):
        #求两个秒的差
        return abs(sec1-sec2)

class WebRisk():
    def __init__(self,logs):
        pass

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