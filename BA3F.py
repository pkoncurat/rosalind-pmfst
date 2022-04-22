def EulerianCycle(D):
    pocetni_cvor=list(D.keys())[0]
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
            for i, elem in enumerate(konacni_put):
                if elem in D:
                    novi_ciklus = konacni_put[i: -1] + konacni_put[:i + 1]
                    konacni_put = novi_ciklus
                    trenutni_cvor = elem
                    break

    return konacni_put 


if __name__=="__main__":
    with open("../Downloads/rosalind_ba3f.txt","r") as f:
        Graph=[line.strip().split(" -> ") for line in f.readlines()]

    D=dict()
    for i in range(len(Graph)):
        D[Graph[i][0]]=Graph[i][1].split(",")

    ciklus=EulerianCycle(D)
    print("->".join(ciklus))

        
