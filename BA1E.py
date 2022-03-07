def StartingPosition(kmer,genome):
    k=len(kmer)
    niz=[]
    for i in range(0,len(genome)-k+1):
        if genome[i:(i+k)]==kmer:
            niz.append(i)
    return niz

def KmerFrequency(kmer,genome):
    count=0
    k=len(kmer)
    for i in range(0,len(genome)-k+1):
        if genome[i:(i+k)]==kmer:
            count=count+1
    return count

def Clump(genome,k,L,t):
    niz=[]
    D=dict()
    for i in range(0,len(genome)-k+1):
        niz.append(genome[i:(i+k)])
    for element in niz:
        novi_niz=StartingPosition(element,genome)
        count=KmerFrequency(element,genome)
        for i in range(0,len(novi_niz)):
            if genome[novi_niz[i]:(novi_niz[i]+L)] and count>=t:
                D[element]=1
    return D

genome=input("Unesite genom: ")
k=int(input("Unesite k: "))
L=int(input("Unesite L: "))
t=int(input("Unesite t: "))
D=Clump(genome,k,L,t)
for x in D.items():
    print(x[0],end=" ")
    
        

