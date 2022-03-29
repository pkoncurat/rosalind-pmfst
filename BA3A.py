def Composition(k,text):
    kmers=[]
    for i in range(0,len(text)-k+1):
        kmers.append(text[i:(i+k)])
    kmers.sort()#elementi niza kmers poredani su po leksikografskom uređaju
    return kmers

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3a.txt","r") as f:
        k=int(f.readline().strip())
        text=f.readline().strip()
    kmers=Composition(k,text)
    for el in kmers:
        print(el)
