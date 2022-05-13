def Expand(leaderboard):
    rez=[]
    for el in leaderboard:
        for elem in mase:
            rez.append(el+[elem])
    return rez      
    
def CycloSpectrum(peptide,integerMassTable):
    masa_cijelog_peptida=sum(peptide)

    niz=[0,masa_cijelog_peptida]

    tmp=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subpeptide=tmp[j:(j+i)]
            masa=sum(subpeptide)
            niz.append(masa)
    niz.sort()
    return niz

def Score(peptide,Spectrum):
    cycloSpectrum=CycloSpectrum(peptide,integerMassTable)

    unikati=set(cycloSpectrum+Spectrum)
    
    count=0
    for el in unikati:
        count+=min(Spectrum.count(el),cycloSpectrum.count(el))
    return count

def Cut(leaderboard,Spectrum,N):
    if len(leaderboard)<=N:
        return leaderboard
    
    D=dict()
    for i,peptide in enumerate(leaderboard):
        D[i]=Score(peptide,Spectrum)

    sortirano=sorted(D.values(),reverse=True)
    
    rez=[leaderboard[key] for key,value in D.items() if value>=sortirano[N-1]]
    return rez
    

def LeaderboardCyclopeptideSequencing(Spectrum,N):
    leaderboard=[[]]
    leaderPeptide=[]

    while len(leaderboard)>0:
        leaderboard=Expand(leaderboard)
        for peptide in leaderboard:
            if sum(peptide)==Spectrum[-1]:
                if Score(peptide,Spectrum)> Score(leaderPeptide,Spectrum):
                    leaderPeptide=peptide
            elif sum(peptide)>Spectrum[-1]:
                leaderboard=[p for p in leaderboard if p!=peptide]
        leaderboard=Cut(leaderboard,Spectrum,N)
    return leaderPeptide


if __name__=="__main__":
    with open("../Downloads/rosalind_ba4g.txt","r") as f:
        N=int(f.readline().strip())
        Spectrum=[int(el) for el in f.readline().strip().split()]
    mase= [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    integerMassTable={'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
         'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
    leaderPeptide=LeaderboardCyclopeptideSequencing(Spectrum,N)
    for el in leaderPeptide:
        elem=str(el)
        print(elem+"-",end="")

