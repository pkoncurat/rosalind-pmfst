def deBrujin(paired_reads):
    D=dict()
    for prvi,drugi in paired_reads:
        D[(prvi[:-1],drugi[:-1])]=(prvi[1:],drugi[1:])
    return D

def EulerianPath(D):
    keys=list(D.keys())
    values=list(D.values())
    
    for i in range(len(keys)):
        if keys[i] not in values:
            prvi_cvor=keys[i]
    for i in range(len(values)):
        if values[i] not in keys:
            zadnji_cvor=values[i]

    #nadimo indeks od prvi_cvor u nizu keys:
    for i in range(len(keys)):
        if keys[i]==prvi_cvor:
            indeks=i
    #uzmemo njegov par u nizu values:
    njegov_par=values[indeks]
    put=[prvi_cvor,njegov_par]

    while njegov_par!=zadnji_cvor:
        for i in range(0,len(keys)):
            if keys[i]==njegov_par:
                index=i
                put.append(values[index])
                njegov_par=values[index]
    return put

#ova funkcija radena je po algoritmu iz zadatka BA3L:
def StringSpelledGappedPatterns(lista,k,d):
    FirstPatterns=[]
    SecondPatterns=[]

    for i in range(0,len(lista)):
        FirstPatterns.append(lista[i][0])
        SecondPatterns.append(lista[i][1])

    PrefixString=FirstPatterns[0]
    SufixString=SecondPatterns[0]
    
    for i in range(1,len(FirstPatterns)):
        PrefixString+=FirstPatterns[i][-1]
        
    for i in range(1,len(SecondPatterns)):
        SufixString+=SecondPatterns[i][-1]

    for i in range(k+d+1,len(PrefixString)):
        if PrefixString[i]!=SufixString[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    return PrefixString+SufixString[len(SufixString)-k-d:]

def StringReconstruction(k,d,paired_reads):
    D=deBrujin(paired_reads)
    path=EulerianPath(D)
    string=StringSpelledGappedPatterns(path,k,d)
    return string


if __name__=="__main__":
    with open("../Downloads/rosalind_ba3j.txt","r") as f:
        k,d=map(int,f.readline().strip().split())
        niz=[line.strip().split("|") for line in f.readlines()]
    print(StringReconstruction(k,d,niz))
