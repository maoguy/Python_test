#-*-coding:utf-8-*-

''' month.py -- by maoguy '''
''' 
要求：输入一个表示月份的数字(1-12)，输出其对应月份名称的缩写
举例：输入--3，输出--Mar. 
方法：利用字符串剪切操作来实现该功能
将所有的月份名称储存在一个字符串中

'''

def main () :
	months = "JanFebMarAprMayJunJulAugSepOctNovDec"
	n = eval (raw_input ("Enter a month number (1 - 12) : "))
	#计算月份n在months中的位置
	pos = (n - 1) * 3
	#计算需要剪切的字符串
	monthAbbrev = months [pos : pos+3]
	#输出结果
	print "The month abbreviation is " , monthAbbrev + "."

if __name__ == '__main__' :	# 运行
	main ()