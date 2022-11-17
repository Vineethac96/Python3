x = int(input("please enter the value\t")) #taking input at run time
print(x+100)

if x<0:  #or if(x<0)
    print("x is negative number")
elif x>0:
    print("x is posiive number")
elif x==0:
    print("x is equal to 0")
else:
    print("not defined")

if True:
    print("PASS")
else: #dead code - as it never reaches the else part as it always evaluates to true
    print("FAIL")

if 10>5: #always evaluates to true
    print("Hii")

#WAP to find highest

a = 10
b = 100
c = 10000

d = 5000

'''if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
    '''

if a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>d:
    print("b is greater")
elif c>d:
    print("c is greater")
else:
    print("d is greater")


total = int(input("enter total amount\t"))
if total<100:
    total = total+10
elif total>=100 and total<=500:
    total = total+50
else:
    total = total+100

print(total)
print("total="+str(total)) #but not +total as total is int type ,cannot concatenate str with int
#or
print(f'{"total="}{total}')  #f-string

