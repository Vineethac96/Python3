#JAVA doesnt support multiple inheritance, but PYTHON supports

class Base1():          #default "object" is super class

    def __init__(self):
        self.str1 = "Vineetha"
        print("Base 1")


class Base2():

    def __init__(self):
        self.str2 = "Blessy"
        print("Base 2")



class Child(Base1, Base2):     #multiple inheritance

    def __init__(self):
        Base1.__init__(self)   #calling constructor from parent classes in this class's constructor
        Base2.__init__(self)

        print("Child")

    def printStrings(self):
        print(self.str1, self.str2)


Demo = Child()
Demo.printStrings()
