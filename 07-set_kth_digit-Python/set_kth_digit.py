# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 


def fun_set_kth_digit(n, k, d):
	c=abs(n)
	result=""
	while(c>0):
		r=c%10
		if(k>0):
			k-=1
		elif(k==0):
			k-=1
			r=d
		c//=10
		result+=str(r)
	while(k>=0):
		k-=1
		result+=str(d)
	if(n<0):
		n=-int(result[::-1])
	else:
		n=int(result[::-1])

	return n

