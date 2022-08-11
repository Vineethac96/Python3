class Car:

    #class variable
    wheels = 4

    #constructor of this class

    def __init__(self):
        print("default constructor")

    def __init__(self,color):
        print("Car class constructor")
        #self.color=color

    def test(self):  #self refers that "this" class or current class
        print("test method")

    #any var declared inside a method = instance variable
    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return self.price

#how to create an object of this class

c1 = Car("Red")

print(c1.wheels)
print(Car.wheels)  #can access by class name also

c1.test()
c1.setPrice(5000)
print(c1.getPrice())

c2 = Car("Black") #in Python we can't do constructor overloading, it always calls latest constructor
c2.setPrice(4000)
print(c2.getPrice())

#Blank class

class Pop:
    pass

p1 = Pop()
