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

def MinimumHammingDistance(pattern,string):
    niz=[]
    for i in range(0,len(string)-len(pattern)+1):
        niz.append(HammingDistance(pattern,string[i:(i+len(pattern))]))
    minimum=min(niz)
    return minimum

def Distance(pattern,Dna):
    suma=0
    for i in range(0,len(Dna)):
        suma+=MinimumHammingDistance(pattern,Dna[i])
    return suma


if __name__ == "__main__":
    with open("../Downloads/rosalind_ba2h.txt", "r") as f:
        pattern = f.readline().strip()
        Dna = f.readline().strip().split(" ")
    distance = Distance(pattern,Dna)
    print(distance)
