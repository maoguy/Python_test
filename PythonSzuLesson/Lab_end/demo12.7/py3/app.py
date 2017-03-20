#_*_coding:utf-8_*_

from flask import *
from weatherQuery import weatherQuery

app = Flask (__name__)

@app.route ("/" , methods = ["GET" , "POST"])
def home () :
    return render_template ("index.html" , weather = "i am laodanfeng") ;

@app.route ("/query" , methods = ["GET"])
def query_form () :
    return render_template ("weatherQuery.html") ;

@app.route ("/query" , methods = ["POST"])
def query () :
    cityName = request.form.get("cityName")
    print (cityName)
    weather = weatherQuery (cityName)
    if (weather != None) :
        print (weather)
        return render_template ("weatherQuery.html" ,  weather = weather)
    else :
        return render_template("weatherQuery.html" , weather = "查询错误(请输入广东省内城市名字)")
@app.route ("/github" , methods = ["GET"])

@app.route ("/picture" , methods = ["GET"])
def picture () :
    pic = url_for ("static" , filename = "foo.jpg")
    return pic

@app.route ("/games" , methods = ["GET"])
def games () :
    return render_template ("games.html")

@app.route ("/snake" , methods = ["GET"])
def snake () :
    return render_template ("snake.html")

if __name__ == "__main__" :
    app.run(host = '0.0.0.0' , debug = True , port = 3000) ;
