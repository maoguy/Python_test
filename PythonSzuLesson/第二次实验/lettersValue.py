#-*-coding:utf-8-*-

''' lettersValue.py -- by maoguy '''

''' 
编写程序，
输入一个字符串表示名字，
计算名字中各个字母数值总和.
'''

def main () :
	theSum = 0	# 定义计数变量
	letters = raw_input ("Please input the string : ") # 输入字符串
	letters2upper = letters.upper ()	# 转化为大写，方便转换
	for theWord in letters2upper :		# 遍历字符串
		theSum = theSum + ord (theWord) - 64	# 字符对应的数值
	print ("The letters you input's sum is : %d ")  %(theSum)	# 输出

if __name__ == '__main__' :	# 运行
	main ()