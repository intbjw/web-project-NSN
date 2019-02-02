#用于解析web目录的一个类
class Log():
    def __init__(self,s):
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
        self.length = int(s[2].split()[1])
        #得到用户提出请求时所在的URL和user-agent
        self.url = s[3]
        self.user_agent = s[5]
