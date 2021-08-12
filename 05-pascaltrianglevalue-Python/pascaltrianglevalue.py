# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

#Using nCr=n!/r!(n-r)!




def fun_pascaltrianglevalue(row, col):
	return fact(row)//(fact(col)*fact(row-col))

def fact(n):
	if(n<=1):
		return 1
	else:
		return n*fact(n-1)
	

print(fun_pascaltrianglevalue(5,2))