def ArrayKmers(k):
    #stvaramo niz od 4^k k-mers
    if k==1:
        return ["A", "C", "G", "T"]
    rezultat=[]
    pomocni=ArrayKmers(k-1)
    for i in ["A", "C", "G", "T"]:
        for j in pomocni:
            rezultat.append(i+j)
    return rezultat   

def PatternCount(text,pattern):
    count=0
    for i in range(len(text)-len(pattern)+1):
        if text[i:(i+len(pattern))]==pattern:
            count+=1
    return count

def FrequencyArray(text,k):
    array_kmers=ArrayKmers(k)
    for pattern in array_kmers:
        print(PatternCount(text,pattern),end=" ")
    
text=input("Unesite text:")
k=int(input("Unesite k:"))
FrequencyArray(text,k)
