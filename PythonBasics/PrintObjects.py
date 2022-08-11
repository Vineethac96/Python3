#string represention of class objects
#Objet printing

class Test:

     def __init__(self,x,y):
         self.x=x
         self.y=y

     def __repr__(self):
         return "a:%s,b:%s" %(self.x,self.y)

     def __str__(self):
         return "value of x is %s and y is %s" %(self.x,self.y)

t = Test(10,20)
print(t)

#if no str method is defined, then repr is called