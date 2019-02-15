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
    #Attack记录攻击次数，每个ip的一次攻击算一次攻击
    Attack = [0,0,0,0,0]
    #按IP划分
    iplist = parseIp(loglist)
    #威胁分析
    risklist = []
    for ip in iplist:
        risk = WebRisk(ip)
        #累加攻击次数
        Attack[0] = risk.DirBusetr_num + Attack[0]
        Attack[1] = risk.CmdExecute_num + Attack[1]
        Attack[2] = risk.PasswdBuster_num + Attack[2]
        Attack[3] = risk.SqlInjection_num + Attack[3]
        Attack[4] = risk.Xss_num + Attack[4]
        risklist.append(risk)
    Attackset = attack.CountAttack(Attack)
    #生成json数据
    makejson(risklist)
    return (URLset,IPset,Attackset)
