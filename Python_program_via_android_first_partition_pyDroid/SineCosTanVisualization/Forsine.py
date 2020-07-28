import math
i=0;
while (i<=360):
	Ans=math.sin((math.pi*i)/(180)) 
	print("*"*50)
	print("{} == {}".format(i,Ans))
	print("*"*50)
	i=i+1
    