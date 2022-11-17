#while loop

count=0
while (count<4):
    print("hello")
    count+=1

num=0
while (num<3):
    print("hi")
    num+=1
else:          #new concept in python, not present in Java
    print("bye")

print("----------")

name = ['Vineetha','Manoj','Shyni','Sumanth']
i=0
while(i<2):
    print(name[i])
    i+=1

print("----------")

#for loop
name = ['Vineetha','Manoj','Shyni','Sumanth']
for i in name:
    print(i)
for i in name[1]:
        print(i)

str = 'IloveYou'
for a in str:
    print(a)

# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and stops before a specified number.(range)
#range(5) - 0,1,2,3,4
#

val = ['Automation','in','Python']
for i in range(2):
    print(val[i])    #list[i] not just i as we are definig range not (for i in list)

for i in range(len(val)): #when just mentioned list, it will print all elements,
    print(val[i])
else:
    print("list is over")

for i in range(3,50,2):      #from 3 to 5 , increment by 2
    print(i)

#nested loops  - pattern
for i in range(1,5):
    for j in range(i):
        print("*",end='')
    print()

for i in range(1,5):
    for j in range(i):
        print(i,end='')
    print()
