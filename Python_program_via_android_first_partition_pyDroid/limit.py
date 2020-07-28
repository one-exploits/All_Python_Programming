import os;
loop,ans=1,0;
limit=float();
	
print("  lim");
print("\nx----->? :");
limit=float(input());
loop=limit;
while(loop<=1000):
	if(loop==1.0):
		loop=loop-0.00000000000001
#		print("\033[31m");
#	else:
#		print("\033[32m")
		
	ans=((loop*loop)-1)/(loop-1);
	print(" f ( {} )  =  {}".format(loop,ans));
	os.system("sleep 0.0")
	loop=loop-0.0000001;
	
	