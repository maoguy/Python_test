from weatherQuery import weatherQuery

cityName = raw_input("cityName:").decode("gb2312").encode("gb2312")
print isinstance (cityName , unicode)

weather = weatherQuery (cityName) ;

print weather
