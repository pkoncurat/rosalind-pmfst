def Expand(peptides):
    novi=[]
    for peptide in peptides:
        for masa in mase:
            novi.append(peptide+[masa])
    return novi
        
def Cyclospectrum(peptide):
    masa_cijelog_peptida=sum(peptide)
    niz=[0,masa_cijelog_peptida]

    tmp=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subpeptid=tmp[j:(j+i)]
            niz.append(sum(subpeptid))
    niz.sort()
    return niz

def Consistent(peptide):
    theoretical_spectrum=[0,sum(peptide)]
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)-i+1):
            subpeptid=peptide[j:(j+i)]
            theoretical_spectrum.append(sum(subpeptid))

    rez=[]
    for el in theoretical_spectrum:
        if el in Spectrum:
            rez.append(True)
        else:
            rez.append(False)
    return rez

def CyclopeptideSequencing(Spectrum):
    peptides=[[]]
    rez=[]
    while len(peptides)>0:
        peptides=Expand(peptides)
        for peptide in peptides:
            if sum(peptide)==Spectrum[-1]:
                if Cyclospectrum(peptide)==Spectrum:
                    rez.append(peptide)
                peptides=[p for p in peptides if p!=peptide]
            elif False in Consistent(peptide):
                peptides=[p for p in peptides if p!=peptide]
    return rez


if __name__=="__main__":
    with open("../Downloads/rosalind_ba4e.txt","r") as f:
        Spectrum=[int(el) for el in f.readline().strip().split()]
    mase=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    rez=CyclopeptideSequencing(Spectrum)
    for el in rez:
        print("-".join(map(str,el)),end=" ")

