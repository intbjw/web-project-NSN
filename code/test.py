import parse
url = '''192.168.169.1 - - [09/Jan/2030:12:44:21 +0800] "GET /search.php?search=11%29%20AND%203913%3D7902%20AND%20%282383%3D2383 HTTP/1.1" 200 2724 "-" "sqlmap/1.0.5.36#dev (http://sqlmap.org)"'''
log  = parse.Log(url)
logs = []
logs.append(log)
risk = parse.WebRisk(logs)
print(risk.isSqlInjection())

print(url)
