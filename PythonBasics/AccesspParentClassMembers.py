class Base(object):

    def __init__(self,x):
        self.x = x


class Child(Base):

    def __init__(self,x,y):
        Base.x = x       #parent class menbers can be accessed in child class by <BaseClassName>.<datamember>  self-means that class
        self.y = y       #child class member "y"

    def printWork(self):
        print(Base.x,self.y)
        print("x =", Base.x, "y =" ,self.y)


#Test Code

ob = Child(10,20)
ob.printWork()
