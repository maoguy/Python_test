#-*-coding:utf-8-*-

''' sphere.py -- by maoguy '''

'''
编写程序，输入球体半径，
计算出球的体积和表面积，
并输出结果. 
'''
from math import *

def surface ( r ) :
	S = 4*pi*sqrt(r)	# 计算球的表面积公式
	return S

def volume ( r ) :
	V = (4.0/3.0)*pi*pow(r , 3)	# 计算球的体积公式
	return V

def main () :
	radius = input ("Please input the radius : ")	# 输入球的半径
	theSurface = surface (radius)
	theVolume = volume (radius)
	# 输出计算结果
	print ("The surface is %f , the Volume is %f .") %(theSurface , theVolume)

if __name__ == "__main__" :	# 运行
	main ()