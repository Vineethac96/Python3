def f1(): #non-parameterized
    print("hello")

f1()   #calling func f1


def test(a): #parameterized function
    print(a+10)

test(10)


#optional/default parameter
def getCountryName(name="India"):
    print(name)

getCountryName()
getCountryName("UK")  #callinf getCountryname with diff input parameter
getCountryName(100)      #change data type also in python
getCountryName([1,2,3])  #change data type also in python

#pass a list to a function
def getnames(list):
    for i in list:
        print(i)

names = ["Vineetha","Manoj","Shyni","Sumanth"]
getnames(names)

#function with return
def sum(a,b):
    c = a+b
    return c      #or return a+b

s1=sum(10,20)
print(s1)
print(sum(50,50))

def getCapitalName(countryName):
    if countryName == "India":
        return "New Delhi"
    elif countryName == "US":
        return "Washington DC"

print(getCapitalName("India"))

def launchbrowser(browser):
    if browser=="Google":
        print("launc chrome")
    elif browser=="Firefox":
        print("launch firefix")
    else:
        print("browser not defined")

launchbrowser("IE")

#Recursion in Python
#factorial of a given number (4*3*2*1)
def factorial(num):
   if(num>1):
       num = num * factorial(num-1)
   return num

print(factorial(5))


def login(username,password):
    print("login with %s and %s" %(username,password))

login("vineetha","test@123")




