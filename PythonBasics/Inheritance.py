class Person(object):  # object is superclass for all classes in python, default "()" means the same

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        self.emp_age = 10
        return self.emp_age


class Employee(Person):  # Empoyee is child class of super class Person

    def isEmployee(self):  # method overriding
        self.emp_age = 20
        return self.emp_age


# Test Person
emp = Person("Vineetha")  # as constructor has name parameter, we should mention name
print(emp.name)
print(emp.getName(), emp.isEmployee())     #isEmployee of Person Class

emp1 = Employee("Blessy")
print(emp1.name)
print(emp1.getName())
print(emp1.isEmployee())                    #isEmployee of Employee Class
