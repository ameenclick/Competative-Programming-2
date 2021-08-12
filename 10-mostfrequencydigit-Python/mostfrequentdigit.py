# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	count={}
	maxi=999
	if(n==0):
		return 0
	while(n>0):
		r=n%10
		n//=10
		if(r in count):
			count[r]+=1
		else:
			count[r]=1
		if(count[r] == max(count.values()) and r<maxi):
			maxi=r
	return maxi

print(mostfrequentdigit(0))