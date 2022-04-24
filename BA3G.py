from collections import Counter

def EulerianCycle(D,start):
    pocetni_cvor=start
    trenutni_cvor=pocetni_cvor
    konacni_put=[pocetni_cvor]

    while D:
        if trenutni_cvor in D:
            konacni_put.append(D[trenutni_cvor][0])
            if len(D[trenutni_cvor])==1:
                 del D[trenutni_cvor]
            else:
                del D[trenutni_cvor][0]
            trenutni_cvor=konacni_put[-1]
        else:
            for i,elem in enumerate(konacni_put):
                if elem in D:
                    novi_put=konacni_put[i:-1]+konacni_put[:i+1]
                    konacni_put=novi_put
                    trenutni_cvor=elem
                    break
    return konacni_put

def add_imaginary_edge(D):
    broj_ulaznih_bridova=Counter()
    broj_izlaznih_bridova=Counter()

    for key,value in D.items():
        broj_izlaznih_bridova[key] += len(value)
        for v in value:
             broj_ulaznih_bridova[v] += 1

    start=list(broj_ulaznih_bridova-broj_izlaznih_bridova)[0]
    end=list(broj_izlaznih_bridova-broj_ulaznih_bridova)[0]

    #dodajemo novi(imaginarni brid):
    D[start]=[end]
    return start,end
    

def EulerianPath(D):
    start,end=add_imaginary_edge(D)
    ciklus=EulerianCycle(D,end)[1:]

    for i in range(len(ciklus)):
        if ciklus[i]==start and ciklus[i+1]==end:
            return ciklus[i+1:]+ciklus[:i+1]
    

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3g.txt","r") as f:
        Graph=[line.strip().split(" -> ") for line in f.readlines()]
    
    D=dict()
    for i in range(0,len(Graph)):
        D[Graph[i][0]]=Graph[i][1].split(",")
    path=EulerianPath(D)
    print("->".join(path))

