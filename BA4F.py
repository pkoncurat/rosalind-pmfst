def CycloSpectrum(peptide,integerMassTable):
    masa_cijelog_peptida=0
    for slovo in peptide:
        masa_cijelog_peptida+=integerMassTable[slovo]

    niz=[0,masa_cijelog_peptida]

    tmp=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subpeptide=tmp[j:(j+i)]
            masa=0
            for slovo in subpeptide:
                masa+=integerMassTable[slovo]
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


if __name__=="__main__":
    with open("../Downloads/rosalind_ba4f.txt","r") as f:
        peptide=f.readline().strip()
        Spectrum=[int(el) for el in f.readline().strip().split()]
    integerMassTable={'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}

    print(Score(peptide,Spectrum))
