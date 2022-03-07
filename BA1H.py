def HammingDistance(pattern1,pattern2):
    niz1=[]
    for slovo in pattern1:
        niz1.append(slovo)
    niz2=[]
    for slovo in pattern2:
        niz2.append(slovo)
    count=0
    for i in range(0,len(niz1)):
        if niz1[i]!=niz2[i]:
            count=count+1
    return count

def ApproximatePattern(pattern,text,d):
    k=len(pattern)
    niz=[]
    for i in range(0,len(text)-k+1):
        if HammingDistance(text[i:(i+k)],pattern)<=d:
            niz.append(i)
    return niz

pattern=input("Unesite pattern:")
text=input("Unesite text: ")
d=int(input("Unesite d: "))
niz=ApproximatePattern(pattern,text,d)
for el in niz:
    print(el,end=" ")
      
