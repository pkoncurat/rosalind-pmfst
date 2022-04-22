def StringReconstruction(patterns,k):
    suffix=[]
    prefix=[]

    D=dict()
    for kmer in patterns:
        suffix.append(kmer[1:])
        prefix.append(kmer[:-1])
        D[kmer[:-1]]=kmer[k-1:k]

    #pronadimo pocetni kmer:
    for p in prefix:
        if p not in suffix:
            start=p
            break

    pocetak_teksta=start+D[start]

    #pronadimo krajnji kmer:
    for s in suffix:
        if s not in prefix:
            end=s
            break

    text=pocetak_teksta
    while True:
        ostatak_teksta=text[len(text)-k+1:len(text)]
        if ostatak_teksta==end:
            break
        else:
            text+=D[ostatak_teksta]
    return text
        
##k=4
##patterns=["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]
##
##print(StringReconstruction(patterns,k))

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3h.txt","r") as f:
        k=int(f.readline())
        patterns=[line.strip() for line in f.readlines()]
    print(StringReconstruction(patterns,k))
