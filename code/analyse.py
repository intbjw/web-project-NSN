from parse import *
def analyseLog(file_name):
    '''
    该函数用于日志扫描部分的代码
    可根据实际需要将函数取消封装
    拆分函数功能,或者修改返回值
    这里只是一个样本
    '''
    loglist = []
    #读取日志文件并解析为列表
    with open(file_name) as f:
        lines = f.readlines()
    for line in lines:
        log = Log(line)
        loglist.append(log)
    #统计
    attack = Statistics()
    URLset = attack.CountURL(loglist)
    IPset = attack.CountIP(loglist)
    Attackset = attack.CountAttack(loglist)
    #按IP划分
    iplist = parseIp(loglist)
    #威胁分析
    risklist = []
    for ip in iplist:
        risk = WebRisk(ip)
        risklist.append(risk)
    #生成json数据
    makejson(risklist)

    return (URLset,IPset,Attackset)
