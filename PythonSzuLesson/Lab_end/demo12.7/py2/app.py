#_*_coding:utf-8_*_

from flask import Flask , request , render_template
from weatherQuery import weatherQuery

app = Flask (__name__) ;

@app.route ("/" , methods = ["GET" , "POST"])
def home () :
    return render_template ("index.html" , weather = "i am laodanfeng") ;

@app.route ("/query" , methods = ["GET"])
def query_form () :
    return render_template ("query.html") ;

@app.route ("/query" , methods = ["POST"])
def query () :
    cityName = request.form["cityName"].encode("gb2312")
    #print cityName
    #a=raw_input ("input:")
    print isinstance (cityName , unicode)
    weather = weatherQuery (cityName)
    #weather = "17"
    return render_template ("weather.html" , cityName = cityName , weather = weather)

@app.route ("/weather" , methods = ["GET"])
def weather () :
    return render_template ("weather.html")

if __name__ == "__main__" :
    app.run() ;
