def login(username,password):
    print("login with %s and %s" %(username,password))

login("vineetha","test@123")
#or
login(username="vineetha",password="test@123")


#non-keyword arguments -The special syntax *args in function definitions in python is used
# to pass a variable number of arguments to a function.
# *arg
def getMarks(*arg):
    for x in arg:
        print(x)

getMarks(10,20,30)
getMarks("A","A+","B")

#Keyword arguments-The special syntax **kwargs in function definitions in python
# is used to pass a keyworded, variable-length argument list
# **arg
def getStudentMarks(**args):
    for key,value in args.items():
        print("%s == %s" %(key,value))

getStudentMarks(vineetha=10,Manoj=20)
getStudentMarks(device="Apple",sellerName="Zeon")


#lambda functions: Anonymous function
#a function without any name
#Lambda functions can take any number of arguments:

cube = lambda x: x*x*x
print(cube(5))

total = lambda marks: marks+30
print(total(100))

x = lambda a, b : a * b
print(x(5, 6))

