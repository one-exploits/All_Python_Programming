print("Hi i am Arquam , in this program i have been showed defect of vision")
y=input("What is your defect of vision [Myopiya : Hypermetropia] enter");
if y=="Myopia":
	x=input("Which is your point , after it you can not see enter either cm:m")
	print(str(x)+ " cn :m please Enter");
	mcm=input();
	print('befire it i want to say that you should have a ^^^^^^^^^^ concave lense^^^^^^^')
	f=-1/float(x)-1/float(-1*0/1);
	focullenth=float(1/f);