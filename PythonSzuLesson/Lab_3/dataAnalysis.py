#-*-coding:utf-8-*-

'''
dataAnalysis.py -- by maoguy
'''

'''
读取文件
数据统计
图表绘制
'''
from graphics import *	#引入图表绘制模块

#数据统计函数 输入：文件名（字符串） 返回：各成绩段统计结果（dict）
def dataAnalysis (fileName) :
    #number = [] ;	
    #name = [] ;

    levelNum = {'a' : 0 , 'b' : 0 , 'c' : 0 , 'd' : 0 , 'e' : 0 , 'f' : 0} ;
	#用变量levelNum（dict类型）来存放格式化的统计结果
    temp = [] ;
    infile = open (fileName , "r") ;	#以读的模式打开文件
    for i in infile.read().split ("\n") :	#以换行符为节点进行分割
        temp.append (i.split()) ;	#以空为节点进行分割
    infile.close() ;

    for i in temp[1:-1] :	#对格式化的List进行遍历统计
        score = eval (i[2]) ;	#将分数转化为可计算的数值形式
        if score < 60 :
            levelNum['f'] += 1 ;	#低于60分为f-level
        elif score < 70 :
            levelNum['e'] += 1 ;	#60-69分为e-level
        elif score < 80 :
            levelNum['d']+= 1 ;		#70-79分为d-level
        elif score < 90 :
            levelNum['c'] += 1 ;	#80-89分为c-level
        elif score < 100 :
            levelNum['b'] += 1 ;	#90-99分为b-level
        elif score == 100 :
            levelNum['a'] += 1 ;	#100分为a-level
			
    return levelNum ;	#将统计结果（dict）作为函数返回值返回

#图表绘制函数 输入：成绩统计结果（dict） 输出：绘制出统计图表
def graph (levelNum) :
    win = GraphWin ("ScoreAnalysis" , 800 , 600) ;	#生成GUI图形界面
    for i in range (0 , 6) :
		#以a、b、c、d、e、f六个level为横坐标
        rect = Text (Point(i*100 + 150 , 550) , chr(97+i)+"-level") ;	
        rect.draw(win) ;

    for i in range (0 , 6) :
		#以0、1、2、3、4、5六个人数作为纵坐标
        rect = Text (Point(50 , 600-i*100) , i) ;
        rect.draw (win) ;

    for i in levelNum :
		#用不同的高度表示不同分数段的人数
        rect = Rectangle (Point((ord(i) - 97)*100+100 , 600-levelNum[i]*100) , Point((ord(i) - 97)*100+200 , 600))
        rect.draw(win) ;

def main () :
    fileName = raw_input ("please input the fileName : ") ;
	#用户输入所需的读取文件的文件名
    temp = dataAnalysis(fileName) ;
	#获得统计结果
    graph (temp) ;
	#绘制统计图表


if __name__ == "__main__" :
    main () ;
