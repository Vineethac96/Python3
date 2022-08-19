class Base(object):
    pass           #Empty class

class Child(Base):
    pass           #Empty class


#Test Code
print(issubclass(Child,Base))    #syntax : issubclass(child class,base class)
print(issubclass(Base,Child))

c = Child()
b = Base()

print(isinstance(b, Base))
print(isinstance(c, Base))   #True coz of inheritance
print(isinstance(b, Child))