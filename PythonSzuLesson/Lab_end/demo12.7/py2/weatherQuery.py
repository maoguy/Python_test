#_*_coding:utf-8_*_
import requests
import json
from city import city

def weatherQuery (cityName) :
    print cityName;
    cityCode = city.get(cityName) ;
    print cityCode
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html') %cityCode

    response = requests.get(url)
    #print content
    #return content.decode('utf8')
    data = json.loads(response.content.decode('utf8'))
    result = data['weatherinfo']
    str_temp = ("%s %s %s ~ %s") % (result['city'] , result['weather'] , result['temp1'] , result['temp2'])
    #print str_temp
    return str_temp
