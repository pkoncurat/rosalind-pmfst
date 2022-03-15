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
            count+=1
    return count

def AllKmers(k):
    if k==1:
        return ["A","C","G","T"]
    rezultat=[]
    pomocni=AllKmers(k-1)
    for i in ["A","C","G","T"]:
        for j in pomocni:
            rezultat.append(i+j)
    return rezultat


def MinHammingDistance(pattern,text):
    niz=[]
    for i in range(0,len(text)-len(pattern)+1):
        niz.append(HammingDistance(pattern,text[i:(i+len(pattern))]))
    minimum=min(niz)
    return minimum

def MedianString(k,Dna):
    kmers=AllKmers(k)
    D=dict()
    for el in kmers:
        suma=0
        for i in range(0,len(Dna)):
            minimum=MinHammingDistance(el,Dna[i])
            suma+=minimum
        try:
            D[el]=suma
        except KeyError:
            D[el]=[suma]

    minimumSvihSuma=min(D.values())
    return D.fromkeys([x[0] for x in D.items() if x[1]==minimumSvihSuma],minimumSvihSuma)


if __name__=="__main__":
    with open("../Downloads/rosalind_ba2b.txt","r") as f:
        k=int(f.readline().strip())
        Dna=[line.strip() for line in f]
    D=MedianString(k,Dna)   
    for x in D.items():
        print(x[0])
