def DeBruijn(Patterns):
    D=dict()
    for kmer in Patterns:
        if kmer[:-1] not in D.keys():
            D[kmer[:-1]]=kmer[1:]
        else:
            D[kmer[:-1]]+=","+kmer[1:]
    return D
    
if __name__=="__main__":
    with open("../Downloads/rosalind_ba3e.txt","r") as f:
        Patterns=[line.strip() for line in f.readlines()]
    D=DeBruijn(Patterns)
    for key in sorted(D.keys()):
        print(key+" -> "+D[key])
