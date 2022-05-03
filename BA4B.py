def ReverseComplement(pattern):
    niz=[]
    for i in range(0,len(pattern)):
        if pattern[i]=="A":
            niz.append("T")
        elif pattern[i]=="T":
            niz.append("A")
        elif pattern[i]=="C":
            niz.append("G")
        elif pattern[i]=="G":
            niz.append("C")
    reverse=('').join(niz)
    return reverse[::-1]

def TranslateRnaIntoPeptid(Rna,geneticCode):
    peptid=""
    for i in range(0,len(Rna),3):
        trimer=Rna[i:(i+3)]
        peptid+=geneticCode[trimer]
    return peptid
    

def PeptideEncoding(Dna,peptid,geneticCode):
    duljina_substringova=len(peptid)*3
    niz=[]
    
    for i in range(0,len(Dna)-duljina_substringova+1):
        kmer=Dna[i:(i+duljina_substringova)]
        reverse=ReverseComplement(kmer)

        kmer=kmer.replace("T","U")
        reverse=reverse.replace("T","U")

        if TranslateRnaIntoPeptid(kmer,geneticCode)==peptid or TranslateRnaIntoPeptid(reverse,geneticCode)==peptid:
            niz.append(kmer.replace("U","T"))
        
    return niz  
        

if __name__=="__main__":
    with open("../Downloads/rosalind_ba4b.txt","r") as f:
        Dna=f.readline().strip()
        peptide=f.readline().strip()
    geneticCode = {
  'AAA': 'K', 
  'AAC': 'N', 
  'AAG': 'K', 
  'AAU': 'N', 
  'ACA': 'T', 
  'ACC': 'T', 
  'ACG': 'T', 
  'ACU': 'T', 
  'AGA': 'R', 
  'AGC': 'S', 
  'AGG': 'R', 
  'AGU': 'S', 
  'AUA': 'I', 
  'AUC': 'I', 
  'AUG': 'M',
  'AUU': 'I', 
  'CAA': 'Q', 
  'CAC': 'H',  
  'CAG': 'Q', 
  'CAU': 'H',
  'CCA': 'P', 
  'CCC': 'P', 
  'CCG': 'P', 
  'CCU': 'P',
  'CGA': 'R',
  'CGC': 'R', 
  'CGG': 'R', 
  'CGU': 'R',
  'CUA': 'L', 
  'CUC': 'L', 
  'CUG': 'L', 
  'CUU': 'L', 
  'GAA': 'E', 
  'GAC': 'D', 
  'GAG': 'E', 
  'GAU': 'D', 
  'GCA': 'A', 
  'GCC': 'A', 
  'GCG': 'A', 
  'GCU': 'A',
  'GGA': 'G', 
  'GGC': 'G', 
  'GGG': 'G', 
  'GGU': 'G', 
  'GUA': 'V' , 
  'GUC': 'V', 
  'GUG': 'V' , 
  'GUU': 'V', 
  'UAA': '', 
  'UAC': 'Y', 
  'UAG': '', 
  'UAU': 'Y', 
  'UCA': 'S', 
  'UCC': 'S', 
  'UCG': 'S', 
  'UCU': 'S', 
  'UGA': '', 
  'UGC': 'C', 
  'UGG': 'W',
  'UGU': 'C',
  'UUA': 'L', 
  'UUC': 'F', 
  'UUG': 'L', 
  'UUU': 'F'
}
    niz=PeptideEncoding(Dna,peptide,geneticCode)
    for el in niz:
        print(el)
