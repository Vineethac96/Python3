#data hiding
# Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected.
# But In Python, we don’t have direct access modifiers like public, private, and protected.
# We can achieve this by using single underscore and double underscores.
# Using encapsulation, we can hide an object’s internal representation from the outside. This is called information hiding

class Employee:

    #hidden data member of Employee class
    __salary = 1000 #private variable


E1 = Employee()
#print(E1.__salary)   #cant access as it is hidden data menmber/private member

#access private/hidden variable using tricky syntax:(_classname__membername)
print(E1._Employee__salary)

