while(True):
    string1=input("Unesi prvi string: ")
    string2=input("Unesi drugi string: ")
    if(len(string1)==len(string2)):
        break

niz1=[]
for slovo in string1:
    niz1.append(slovo)

niz2=[]
for slovo in string2:
    niz2.append(slovo)

count=0
for i in range(0,len(niz1)):
    if niz1[i]!=niz2[i]:
        count=count+1
print(count)
