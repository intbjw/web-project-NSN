
import geoip2.database

reader = geoip2.database.Reader(
    '../ipdata/GeoLite2-City.mmdb')


def ip_print_AddrInfo(ip):

    # 载入指定IP相关数据
    response = reader.city(ip)
    # 读取国家代码
    Country_IsoCode = response.country.iso_code
    # 读取国家名称
    Country_Name = response.country.name
    # 读取国家名称(中文显示)
    Country_NameCN = response.country.names['zh-CN']
    # 读取州(国外)/省(国内)名称
    Country_SpecificName = response.subdivisions.most_specific.name
    # 读取州(国外)/省(国内)代码
    Country_SpecificIsoCode = response.subdivisions.most_specific.iso_code
    # 读取城市名称
    City_Name = response.city.name
    # 读取邮政编码
    City_PostalCode = response.postal.code
    # 获取纬度
    Location_Latitude = response.location.latitude
    # 获取经度
    Location_Longitude = response.location.longitude
    # ------------------------------------------------打印
    print('[*] Target: ' + ip + ' GeoLite2-Located ')
    print('  [+] Country_IsoCode        : ' + Country_IsoCode)
    print('  [+] Country_Name           : ' + Country_Name)
    print('  [+] Country_NameCN         : ' + Country_NameCN)
    print('  [+] Country_SpecificName   : ' + Country_SpecificName)
    print('  [+] Country_SpecificIsoCode: ' + Country_SpecificIsoCode)
    print('  [+] City_Name              : ' + City_Name)
    if City_PostalCode != None:
        print('  [+] City_PostalCode        : ' + City_PostalCode)
    print('  [+] Location_Latitude      : ' + str(Location_Latitude))
    print('  [+] Location_Longitude     : ' + str(Location_Longitude))


ip = '27.186.96.72'
ip_print_AddrInfo(ip)