def ArrayKmers(k):
    if k==1:
        return ["A","C","G","T"]
    pomocni=ArrayKmers(k-1)
    rezultat=[]
    for i in ["A","C","G","T"]:
        for j in pomocni:
            rezultat.append(i+j)
    return rezultat

def HammingDistance(p,q):
    niz1=[]
    for slovo in p:
        niz1.append(slovo)
    niz2=[]
    for slovo in q:
        niz2.append(slovo)
    count=0
    for i in range(0,len(niz1)):
        if niz1[i]!=niz2[i]:
            count=count+1
    return count

def Neighbours(pattern,d):
    k=len(pattern)
    array_kmers=ArrayKmers(k)
    rezultat=[]
    for el in array_kmers:
        if HammingDistance(el,pattern)<=d:
            rezultat.append(el)
    return rezultat

pattern=input("Unesite pattern:")
d=int(input("Unesite d:"))
niz=Neighbours(pattern,d)
for el in niz:
    print(el)
