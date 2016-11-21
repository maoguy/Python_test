#_*_coding:utf-8_*_

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route ('/' , methods = ['GET' , 'POST'])
def home () :
	return render_template ('home.html')

@app.route ('/signin' , methods = ['GET'])
def signin_form () :
	return 	render_template ('form.html')

@app.route ('/signin' , methods = ['POST'])
def singin () :
	username = request.form['username']
	password = request.form['password']
	#从request对象中读取表单的内容
	if username == 'admin' and password == 'password' :
		return render_template ('signin-ok.html' , username = username)
	else :
		return render_template ('form.html' , message = 'Bad username or password' , username = username)

if __name__ == "__main__" :
	app.run ()