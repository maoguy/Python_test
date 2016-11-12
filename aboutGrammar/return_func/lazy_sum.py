#an example about return a function

def lazy_sum (*args) :
	def sum () :
		ax = 0
		for n in args :
			ax = ax + n
		return ax
	return sum
	
f = lazy_sum (1,2,3,4,5,6,7,8,9)

print "output f :",f

print "output f() :",f()
