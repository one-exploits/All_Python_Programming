import math



class Triangle:
    def __init__(self,base,height):
        self.base=base;
        self.height=height;
"""
classs about:
    **
    * *
    *  *    hypotenus
opp.*   *
    *    *
    *     *
    ********
       
    adjacent
"""

class Righttriangle(Triangle):
    def __init__(self,hypotenuse,opposite,adjacent):
        if(hypotenuse=="?"):
            Hypo=math.sqrt((opposite**2)+(adjacent**2));
            self.hypotenuse=Hypo;
            self.opposite=opposite;
            self.adjacent=adjacent;

        
                        
        elif(opposite=="?"):
            Oppo=math.sqrt((hypotenuse**2)-(adjacent**2))
            self.opposite=Oppo;
            self.hypotenuse=hypotenuse;
            self.adjacent=adjacent;




        elif(adjacent=="?"):
            Adja=math.sqrt((hypotenuse**2)-(opposite**2))
            self.adjacent=Adja;
            self.hypotenuse=hypotenuse;
            self.opposite=opposite;




        elif(hypotenuse>=0 and opposite>=0 and adjacent>=0):
            self.hypotenuse=hypotenuse
            self.opposite=opposite
            self.adjacent=adjacent;



#       adjacent
#       ********
#       **     *
#       * *    *
# oppos.*  *   *opposite
#       *   *  *
#       *     **
#       *      *
#       ********
#        adjacent

#Are of above=adjacent×opposite;
#So,
#  AreTriangle=(adjacent×opposite)/2
#This function may calculate Are triangle
#


    def Area(self):
        AreaofTriangle=(self.adjacent*self.opposite)/2
        return str(AreaofTriangle)+" unit²";
                   
                   
                   
                   
    def Sin(self):
    	Ans=float();
    	Ans=self.opposite/self.hypotenuse;
    	return Ans               
            

#-----------------------------------------------------------------        
#++++++++++
#ifing for calculate if tow were given
#++++++++++                                          
hhh=Righttriangle(7.8,"?",6);
print(hhh.Sin())

