'''
Dict:key-value pair
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
'''

data = {
      "Vineetha":948,
      "Manoj":917,
      "Shyni":944,
      "Sumanth":986,
        1: "Dad",
        2: "Mom"
}

print(data)
print(data.values())
print(data.keys())
print(data.items()) #prints tuple of each key-value pair
print(data["Shyni"])

print(data[2])
#or access elements using get
print(data.get(2))
print(data.get("Sumanth"))

#pop-removing
print(data.pop(1))
print(data)

#modify
data[1]="Granny"
print(data)

#create a dict from list
keys = ["Hello","World"]
values = [1,2]
data1 = dict(zip(keys,values))
print(data1)
print(data1["World"])

#or

mydict = dict(k='hello',g='hi')
print(mydict)

#add or update dict
data1["Hi"] = 3
print(data1)

#del
del data1["World"]
print(data1)

#list and dict inside a dictionary

prog = {'JS':'Atom', 'Python':['Pycharm','Pytest'], 'Java': {'JSE':'Netbeans', 'JEE':'Eclipse'} }
print(prog)
print(prog['Python'])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JEE'])

#clear
print(data)
data.clear()
print(data)


#loop dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#to print keys
for x in thisdict:
  print(x)

#or
print("-----")
for x in thisdict.keys():
    print(x)

print("-----")
#to print values
for x in thisdict:
    print(thisdict[x])

#or
print("-----")
for x in thisdict.values():
    print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x,"=", y)


#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004,
  "interests" : {"Maths","Science"}
}
child2 = {
  "name" : "Tobias",
  "year" : 2007,
  "interests" : ("TV","Cooking")
}
child3 = {
  "name" : "Linus",
  "year" : 2011,
  "interests" : [10,20]
}

myfamily = {
  "C1" : child1,
  "C2" : child2,
  "C3" : child3
}

print(myfamily)
print(myfamily.values())

