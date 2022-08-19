'''
Collections in Python = List,dict,set,tuple   *Interview QA*
Lists are used to store multiple items in a single variable.(collection of ordered,mutable data)
Python has a great built-in list type named "list".
List literals are written within square brackets [ ].
List can have same or diff data types.  list = [1,2,3,'a','hello',40.8]
Lists work similarly to strings -- use the len() function and square brackets [ ] to access data,
with the first element at index 0.

Assignment with an = on lists does not make a copy.
Instead, assignment makes the two variables point to the one list in memory.

The "empty list" is just an empty pair of brackets [ ].
The '+' works to append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4]
(this is just like + with strings)
 '''

score = [10,20,30,40,50]
print(score)
print(len(score))
print(score[4])
print(score[-2])
print(score[1:3]) #from 1-2

print(score + [1,2,3]) #concatenation
print(score+ ["hi","hello"])

score[2] = 100
print(score)

#append
score.append(60)
print(score)

score.append(5**3) #cube of 5
print(score)

num = ['a','b','c','d','e','f']
print(num)
num[2:5] = ['C','D','E']
print(num)

#remove elements from list
num[2:5] = [] # removes 2 and 3th elements
print(num)

num[:] = [] #entire list is made empty
print(num)
num.append([1,2,3,'a'])
print(num)

#nested lists

a = ["hi", "hello"]
b = [1,2,3]
c = [a,b]
print(c)
print(c[0])
print(c[1])
print(c[0][1])
print(c[1][2])
