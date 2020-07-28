import os;
x=0.8
count=100
while(x<=count):
	function=((x**2)+1)/(x-1);
	print("f({})  = {}".format(x,function))
	os.system("sleep {}".format(str(x/100)));
	x=x+0.001;