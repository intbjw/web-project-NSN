#用于解析web目录的一个类
import time
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
        #这样分割没有记录与0时区的时差，日期也需要进一步分割
        self.date = s[0].split()[-2][1:]
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
        else:
            print("新的未知错误")
        #得到用户提出请求时所在的URL和user-agent
        self.url = s[3]
        self.user_agent = s[5]
class WebDate():
    #29/Jan/2019:06:28:10
    def __init__(self,date):
        self.raw_date = date
        self.second = self.timesec(date)

    @staticmethod
    def timesec(date):
        date = date.split("/")
        #day = date[0]
        #month = date[1]
        date = date[2].split(":")
        #year = date[0]
        hour = date[1]
        minute = date[2]
        sec = date[3]
        #first_year = 2000
        all_sec = 0
        #计算一共多少秒
        '''
        for i in range(first_year,int(year)):
            if i%400==0 or (i%4==0 and i%100 != 0):
                all_sec += 366*24*3600
            else:
                all_sec += 365*24*3600
        '''
        all_sec = int(hour)*3600+int(minute)*60+int(sec)
        return all_sec

    def timeminutes(self,s1,s2=None):
        if s2 == None:
            return self.second - s2.second
        else:
            return s1 - s2
        #注意大小关系
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