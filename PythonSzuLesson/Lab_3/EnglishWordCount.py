#-*-coding:utf-8-*-

'''
EnglishWordCount.py -- by maoguy
'''

'''
编写程序，计算用户输入的英文句子中的词语数量，
以及词语平均长度，输出计算结果。
'''

def main () :
	userInput = raw_input ("Please input a sentence : ") ;
	#获取将用户输入的数据并用变量userInput指示
	wordNum = 0.0 ;		#单词计数变量
	wordLength = 0.0 ;	#单词长度变量
	wordLengthSum = 0.0 ;	#所有单词长度的和
	userInput = userInput.split() ;	#把字符串分割成字符串数组
	
	for word in userInput :		#遍历每一个单词
		wordNum += 1.0 ;		#单词计数变量自增加1
		wordLength = len(word) ;	#计算单词长度
		wordLengthSum += wordLength ;	#计算单词长度之和
		
	#将所需结果打印出来
	print "The wordNum is : " , int(wordNum) ;
	print "The average wordLength is : " , wordLengthSum/wordNum ;
	
if __name__ == "__main__" :
	main () ;
	