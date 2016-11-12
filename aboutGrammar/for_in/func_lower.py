# -*- coding : utf-8 -*-

L1 = ['Hello','World',18,'Apple',None]
L2 = []

for ch in L1 :
	if isinstance (ch,str) :
		L2.append (ch.lower())
	else :
		pass
		
print L2
