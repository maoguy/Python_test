#Higher-order function

def add (x,y,f = abs) :
	return f(x) + f(y)
	
print ("please input x and y , than we will ouput their absolute sum .")
x = int (raw_input ("please input the x :"))
y = int (raw_input ("please input the y :"))

print "|x| + |y| =",add (x,y)
