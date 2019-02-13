import parse
url = '''192.168.189.130 - - [10/Feb/2019:18:36:18 +0800] "GET /search.php?search=%3Ca+selecthref%3D%22http%3A%2F%2Fwww.baidu.com%22%3Esdsds%3C%2Fa%3E HTTP/1.1" 200 2738 "http://192.168.189.129/search.php?search=1111" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"'''
log  = parse.Log(url)
logs = []
logs.append(log)
risk = parse.WebRisk(logs)
print(risk.isSqlInjection())

print(url)