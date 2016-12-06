#_*_coding:utf-8_*_
import urllib2
import json
from city import city
cityName = raw_input ("Please input the CityName of the Weather you want to know:") ;

cityCode = city.get(cityName) ;

url = ('http://www.weather.com.cn/data/cityinfo/%s.html') %cityCode

content = urllib2.urlopen(url).read()

data = json.loads(content)
result = data['weatherinfo']
str_temp = ("%s %s %s ~ %s") % (result['city'] , result['weather'] , result['temp1'] , result['temp2'])

print (str_temp)
