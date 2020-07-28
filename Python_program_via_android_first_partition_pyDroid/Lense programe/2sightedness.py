print ("What is your sightedness [ Myopia : Hypermetropia: ]");
x=input('');
if x=='Myopia':
	print("Which point exist, after it you can not see  ");
	zv=int(float(input()));
	f=float((-1/zv));
	print(f)
	Total=float(1/f);
	print("************");
	print('Your lense is concave lense and its focul length 	=[  ' +str(Total)+' =] ok!');
	print('*************')
	p=float(1/Total);
	print('Power of your lense is  p=	['+str(p)+'] DIOPTER');
	print('thank you for used  program!!');
if x=='Hypermetropia':
	print()
	print();
	print("Okay ! your defect is ` "+str(x)+' `');
	print();
	print ('which is your point, before it you can not see ');
	zxx=int(float(input()));
	print(str(zxx)+' meter or centiMeter Enter either [m:c]');
	mcm=input();
	v=float(-1/zxx);
	u=float(25);
	if mcm=='m':
		u=float(25/100);
	Tu=float(-1/u);
	ff=float(v-Tu);
	Tf=float(1/ff);
	print('*********************')
	print('ou should have a convex lense and its focul length =* '+str(Tf)+'   Okay');
	print("********************")
	print('thank you for using program ');
	
	
		
	
	

	