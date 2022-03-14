def AllKmers(k):
    if k==1:
        return ["A","C","G","T"]
    result=[]
    pomocni=AllKmers(k-1)
    for i in ["A","C","G","T"]:
        for j in pomocni:
            result.append(i+j)
    return result

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


def KmersWithMismatches(pattern,d,skup):
    #stvaramo skup k-mers koji se razlikuju od pattern za d slova
    kmers=AllKmers(len(pattern))
    for element in kmers:
        if HammingDistance(element,pattern)<=d:
            skup.add(element)
    

def MotifEnumeration(Dna,k,d):
    patterns=[]
    for i in range(len(Dna)):
        pattern=set()
        for j in range(len(Dna[i])-k+1):
            kmers=set()
            KmersWithMismatches(Dna[i][j:j+k],d,kmers)
            for el in kmers:
                pattern.add(el)
        for r in pattern:
            patterns.append(r)

    rezultat=[]
    for el in patterns:
        if patterns.count(el)==len(Dna):
            rezultat.append(el)
    rezultat=list(set(rezultat))
    return  rezultat
            
            

if __name__=="__main__":
    with open("../Downloads/rosalind_ba2a.txt","r") as f:
        k,d=map(int,f.readline().strip().split())
        Dna=[line.strip() for line in f]
    rezultat=MotifEnumeration(Dna,k,d)
    for el in rezultat:
        print(el,end=" ")
