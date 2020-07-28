
def factor(n):
	i=0
	x=1;
	while(i<n):
		x=x*(n-i);
		i=i+1;
		print(x,"\n\n")
	return x
	
	
print(factor(10000))
