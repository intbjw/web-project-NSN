import requests
#采用百度的api
import json
def ip2address(ip):
    r = requests.get('http://api.map.baidu.com/location/ip?ip='+ip+'&ak=X7K1gs9RPEoakNnYOtcIgPeMaqGu7TVu&coor=bd09ll')
    result = r.json()
    city = result['content']['address_detail']['city']
    return city


