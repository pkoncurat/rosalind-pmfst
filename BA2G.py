import random

def Vjerojatnost(pattern,profile):
    p=1
    for x in enumerate(pattern):
        p*=profile[x[1]][x[0]]
    return p

def getKmers(text, k):
    kmers = set()
    for i in range(0, len(text) - k + 1):
        kmers.add(text[i:(i+k)])
    return kmers

def profileMostProbable(text,k,profile):
    max_kmer=""
    max_p=-1
    kmers=getKmers(text,k)
    for kmer in kmers:
        p=Vjerojatnost(kmer,profile)
        if p>max_p:
            max_kmer=kmer
            max_p=p
    return max_kmer

def get_motifs(Dna,profile,k):
    motifs=[]
    for motif in Dna:
        motifs.append(profileMostProbable(motif,k,profile))
    return motifs    

def createProfileMatrix(Dna,pseudocounts=False):
    k=len(Dna[0])
    profile=dict()
    
    profile["A"]=[0]*k
    profile["C"]=[0]*k
    profile["G"]=[0]*k
    profile["T"]=[0]*k

    for pattern in Dna:
        for x in enumerate(pattern):
            profile[x[1]][x[0]]=profile[x[1]][x[0]]+1

    if pseudocounts:
        profile["A"]=[x+1 for x in profile["A"]]
        profile["C"]=[x+1 for x in profile["C"]]
        profile["G"]=[x+1 for x in profile["G"]]
        profile["T"]=[x+1 for x in profile["T"]]

    for i in range(0,k):
        suma=profile["A"][i]+profile["C"][i]+profile["G"][i]+profile["T"][i]
        profile["A"][i]=profile["A"][i]/suma
        profile["C"][i]=profile["C"][i]/suma
        profile["G"][i]=profile["G"][i]/suma
        profile["T"][i]=profile["T"][i]/suma

    return profile


def score(motifs):
    zzip = zip(*motifs)

    max_count = []
    for x in zzip:
        n_a = sum([y == "A" for y in x])
        n_c = sum([y == "C" for y in x])
        n_g = sum([y == "G" for y in x])
        n_t = sum([y == "T" for y in x])
        max_count.append(len(motifs) - max(n_a, n_c, n_g, n_t))

    return sum(max_count)

def randomKmers(Dna,k):
    motifs=[]
    n=len(Dna[0])
    for pattern in Dna:
        rand=random.randint(0,n-k)
        kmer=pattern[rand:(rand+k)]
        motifs.append(kmer)
    return motifs

def GibbsSamplerAtom(Dna,k,t,N):
    motifs=randomKmers(Dna,k)
    bestmotifs=motifs

    for j in range(1,N+1):
        i=random.randint(0,t-1)
        tmp=list(motifs)
        tmp.pop(i)
        profile=createProfileMatrix(tmp,pseudocounts=True)
        motifs[i]=profileMostProbable(Dna[i],k,profile)
    
        if score(motifs) < score(bestmotifs):
            bestmotifs = list(motifs)
     
    return bestmotifs

def GibbsSampler(Dna,k,t,N,repeats=20):
    bestmotifs = GibbsSamplerAtom(Dna, k,t,N)
    for i in range(1,repeats+1):
        motifs = GibbsSamplerAtom(Dna, k,t,N)
        if score(motifs) < score(bestmotifs):
            bestmotifs = list(motifs)
    return bestmotifs

if __name__=="__main__":
    with open("../Downloads/rosalind_ba2g.txt","r") as f:
       k,t,N=map(int,f.readline().strip().split())
       Dna=[line.strip() for line in f.readlines()]
    rez=GibbsSampler(Dna,k,t,N,repeats=20)
    for el in rez:
        print(el)
