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
        self.adjacent=adjacent;
        self.hypotenuse=hypotenuse;
        self.opposite=opposite;  

        if(hypotenuse=="?"):
            pass
  

#"""
#Function name:"Hypo();"


#Hypo==hypotenuse;       
#                           
#         *
#         * *
#         *  *
#         *   *
#opposite *    *  hypotenuse==??
#         *     *
#         *      *
#         *********       
#         adjacent

#hypo**2=opp**2  + adja**2

#This function may calculate Hypotenuse:
#"""
    def Hypo(self):
        Ans=math.sqrt((self.opposite**2)+(self.adjacent**2));
        return Ans;


#------------------------------------------------------------------------
#"""
#Function name:"Oppo();"


#Oppo==opposite;       
#                           
#         *
#         * *
#         *  *
#         *   *
#oppo==?? *    *  hypotenuse
#         *     *
#         *      *
#         *********       
#         adjacent

#oppo**2==hypo**2  - adja**2

#This function may calculate Oppsite:
#"""
    def Oppo(self):
        Ans=math.sqrt((self.hypotenuse**2)-(self.adjacent**2))
       
                    

#-----------------------------------------------------------------        
#++++++++++
#ifing for calculate if tow were given
#++++++++++                                          
hhh=Righttriangle(144,23,24);


