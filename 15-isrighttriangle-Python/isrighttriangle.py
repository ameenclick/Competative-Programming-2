# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	a=distance(x1,y1,x2,y2)
	b=distance(x3,y3,x2,y2)
	c=distance(x3,y3,x1,y1)
	altbase=0
	if(a>b):
		if(a>c):
			h=a
			altbase=(b**2+c**2)
		else:
			h=c
			altbase=(b**2+a**2)
	else:
		if(b>c):
			h=b
			altbase=(a**2+c**2)
		else:
			h=c
			altbase=(b**2+a**2)
	if(math.isclose(h**2,altbase)):
		return True
	else:
		return False

def distance(x1,y1,x2,y2):
	return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
