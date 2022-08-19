'''Tuple = is a collection of elements of any python data type.
List vs Tuple": they are similar but
 1. Syntax: List is [], Tuple is ()
 2. Tuple is immutable, but list is mutable
 cannot change value of tuple elements
'''

marks = (10,20,30)
employeeData = ("Tom","25",'m', 23.3, True)  #diff data type

print(employeeData[0])
print(employeeData[3],employeeData[2])
#print(employeeData[5])   out of range
print(employeeData[-1])

list = [10,20,30,40]
list[2] = 60
print(list)    #list is mutable i.e. values can be changed

#immutable0 cannot chnage elements
names = ("Java", "C", "Python")
#names[1]= "C++"      TypeError: 'tuple' object does not support item assignment
del names


t1 = (1,2,3,4)
t2 = (5,6,7,8)

#len
print(len(t2))

#concatenation
print(t1+t2)
print(t2*4)

#slicing
print(t1[2:])
print(t2[-3:])
print(t1[1:3])

#in
print(8 in t2)
print(50 in t1)

#max/min
print(max(t2))
print(min(t1))
names = ("Java", "C", "Python")
print(max(names))  #alphabetical order
print(min(names))



