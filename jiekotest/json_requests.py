import json,requests

r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
print(r.text)
dic=json.loads(r.text)
print(dic,u'数据类型：',type(dic))