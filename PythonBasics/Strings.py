s1 = "Hello Vineetha"
s2 = "Hello Manoj"

print(s1[0])  #access by index
print(s1[-3])
#print(s1[14]) # IndexError: string index out of range
print(s1[0:5]) #slicing - prints from 0th position to 4th
print(s2[4:])   # 4th to end
print(s1[:4])   #first to 3rd position
print(s2[-4:-2])


print(s1+" "+s2)

#escape char
print("hello\nShyni") #print in new line
print("hello\tShyni") #print tab space

print("test"*5) #prints a string 5 times

print("Man" in s2)
print("Java" in s1)
print("java" not in s2)

print("My name is %s and age is %d" %("Vineetha",25))  #formatting operator

s3 = '''hello
guys'''
print(s3)

s4 = """How are
you"""
print(s4)

# For quotes within quotes use \ before the quotes
s5 = 'Hi, I\'m Vineetha'
print(s5)
s6 = "How are you and \"Shyni\" ?"
print(s6)

#String Methods(built-in)
str  = "home sweet home"
print(str.capitalize()) #only first letter is acpitalized
print(str.upper()) #entire string is capitalized

str1 = "HOME"
print(str.lower())

print(str.count("home")) #no of occurences

print(str.find("sweet")) #gives position/index
print(str.find("blessy")) #gives -1 if not found

print(len(str)) #gives length

str2 = " hello people "
print(str2.lstrip()) #strips left whitesapces
print(str2.rstrip()) #strips right whitesapces
print(max(str2)) #max alphabetic(order wise)

str3 = "abcde"
print(min(str3)) #min alphabetic(order wise); even space has lowest order

str4 = "you are sweet"
print(str4.replace("sweet","aka"))
print(str4.split()) #splits and returns a list of words in the string
print(str4.split("are")) #excludes "are"

str5 = str4.split()
print(str5[1])

a = "test"
b = "test"
c = "exam"

#gives boolean result
print(a is b)
print(a is c)
print(a is not c)
print(a == b)
