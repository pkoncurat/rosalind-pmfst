def StartingPositions(pattern,genome):
    k=len(pattern)
    niz=[]
    for i in range(0,len(genome)-k+1):
        if genome[i:(i+k)]==pattern:
            niz.append(i)
    return niz

pattern=input("Unesite pattern: ")
genome=input("Unesite genom: ")
niz=StartingPositions(pattern,genome)
for i in range(0,len(niz)):
    print(niz[i],end=" ")
