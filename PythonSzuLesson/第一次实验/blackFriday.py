# -*-coding:utf-8-*-

# Python程序设计作业，找出黑色星期五

theYear = input ("Please input the year you want to konw : ")

theFirstDay = input ("What day is theFirstDay (1 , 2 , 3 , 4 , 5 , 6 , 7) : ")

day = 1			# 天数计数变量

bigMonth = [1 , 3 , 5 , 7 , 8 , 10 , 12]
smallMonth = [4 , 6 , 9 , 11]

if ((theYear % 4 == 0) and (theYear % 100 != 0)) or (theYear % 400 == 0) :
	print u"这是闰年,二月份有29日"

	for theMonth in range (1 , 13) :
		if theMonth in bigMonth :
			for theDay in range (1 , 32) :
				if (theDay == 13) and (day % 7 == 5) :
					print "The day is black Friday : %d / %d / %d " %(theYear , theMonth , theDay) 
				day = day + 1	# 每轮一天即将天数计数变量加一  
		elif theMonth in smallMonth :
			for theDay in range (1 , 31) :
				if (theDay == 13) and (day % 7 == 5) :
					print "The day is black Friday : %d / %d / %d " %(theYear , theMonth , theDay) 
				day = day + 1	# 每轮一天即将天数计数变量加一
		else :
			 for theDay in range (1 , 30) :
			 	if (theDay == 13) and (day % 7 == 5) :
					print "The day is black Friday : %d / %d / %d " %(theYear , theMonth , theDay) 
			 	day = day + 1	# 每轮一天即将天数计数变量加一

else :
	print u"这是平年，二月份有28日"

	for theMonth in range (1 , 13) :
		if theMonth in bigMonth :
			for theDay in range (1 , 32) :
				if (theDay == 13) and (day % 7 == 5) :
					print "The day is black Friday : %d / %d / %d " %(theYear , theMonth , theDay) 
				day = day + 1	# 每轮一天即将天数计数变量加一  
		elif theMonth in smallMonth :
			for theDay in range (1 , 31) :
				if (theDay == 13) and (day % 7 == 5) :
					print "The day is black Friday : %d / %d / %d " %(theYear , theMonth , theDay) 
				day = day + 1	# 每轮一天即将天数计数变量加一
		else :
			 for theDay in range (1 , 29) :
			 	if (theDay == 13) and (day % 7 == 5) :
					print "The day is black Friday : %d / %d / %d " %(theYear , theMonth , theDay) 
			 	day = day + 1	# 每轮一天即将天数计数变量加一