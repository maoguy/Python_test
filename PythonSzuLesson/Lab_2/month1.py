#-*-coding:utf-8-*-

''' month1.py -- by maoguy '''
''' 
要求：输入一个表示月份的数字(1-12)，输出其对应月份名称
举例：输入--3，输出--March. 
方法：利用List来实现该功能
将所有的月份名称储存在一个List中

'''

def main () :
	months = ["January" , "February" , "March" ,\
				 "April" , "May" , "Jun" , "July" ,\
				  "August" , "September" , "October" ,\
				   "November" , "December"]
	n = eval (raw_input ("Enter a month number (1 - 12) : "))
	#计算月份n在months中的位置
	pos = (n - 1)
	#计算需要剪切的字符串
	monthAbbrev = months [pos]
	#输出结果
	print "The month abbreviation is " , monthAbbrev + "."

if __name__ == '__main__' :	# 运行
	main ()
