'''list and tuple are order based,
Set: is unoredered and syntax {}
1.stores diff data types
2.it performs diff mathematical operations
3.does not store duplicate elements
'''


s1 = {10,20,30,'Tom',12.33,False}
#print(s1[3]) #as it is not ordered, we cannot index numbers
print(s1)    #prints randomly, un-ordered

#doesn't store dupliacte
s2 = {1,2,2,3,4,5,4,2,1}
print(s2)                              #prints {1,2,3,4,5}

#set() function
s3 = set("Python")                     #creates a set object
print(s3)                              #{'n', 'y', 'h', 'o', 't', 'P'}

s4 = set([10,20,30,10])                #converts list to set and removes duplicates
print(s4)

s5 = set((20,45,57,45))                #coverts tuple to set
print(s5)


#while creating a set object, we can store only Numbers,strings,tuple
#List and dict are not allowed, we can pass in set() function, but not while creating

set1 = {10,20,(40,50),90}
print(set1)

#set2 = {15,60,[4,6]}
#print(set2)                             #TypeError: unhashable type: 'list'

#set operations
#union: |
p1 = {1,2,3,33.3,"Blessy"}
p2 = {4,5,6,"Tom",56,2}
print(p1|p2)
print(p1.union(p2))
print(p2.union(p1))

#intersection: &  (Common)
print(p1&p2)
print(p1.intersection(p2))
print(p2.intersection(p1))

#differnece of sets: - (removes common elements)
print(p1-p2)             #{1, 3, 'Blessy', 33.3}
print(p1.difference(p2))
print(p2-p1)             #{4, 5, 6, 'Tom', 56}
print(p2.difference(p1))

#symmateric differnece: ^   :removes duplicates
print(p1^p2)
print(p2.symmetric_difference(p1))


#Set : in-built methods

#1. add()

s1 = {"Java","Python","C++"}
s1.add("Perl")
print(s1)

#2. update(): add mulitile elements

s1.update(["C++","Ruby"])
print(s1)

s1.update(("VBA","C"))
print(s1)

#3. clear
s1.clear()
print(s1)     #blank set

#4. copy
s1 = {1,2,3,"Blessy"}
s2 = s1.copy()
print(s2)

#5. disard
s1.discard(3)
print(s1)

#6. remove
names  = {"Blessy","Java", "C++"}
names.remove("Blessy")
print(names)