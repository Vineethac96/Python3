#data hiding
class Employee:

    #hidden data member of Employee class
    __salary = 1000 #private variable


E1 = Employee()
#print(E1.__salary) #cant access as it is hidden data men=mber/private member

#access private/hidden variable using tricky syntax:(_classname__membername)
print(E1._Employee__salary)
print(t)