name = "Vineetha"
#break-With the break statement we can stop the loop before it has looped through all the items:
for i in name:
    if (i=='t'):
        break
    print(i)

#continue-With continue statement we can stop current iteration of the loop, and continue with the next:
for i in name:
    if (i=='t'):
        continue
    print(i)

name = ['Vineetha','Manoj','Shyni','Sumanth']
flag=False
for i in range(len(name)):
    if(name[i]=='Shyni'):
        flag=True
        break
    print(name[i])
if(flag):
    print("it works")

'''say we have a array list of links, we search for a particular link with 'if' and if found perform click and break'''


for i in range(len(name)):
    if(name[i]=='Shyni'):
        continue
    print(name[i])
