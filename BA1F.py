def MinimumSkew(genome):
    pozicija=0
    niz_pozicija=[]
    for slovo in genome:
        if slovo=="C":
            pozicija+=-1
        elif slovo=="G":
            pozicija+=1
        niz_pozicija.append(pozicija)
    minimum=min(niz_pozicija)
    rezultat=[]
    for i in range(0,len(niz_pozicija)):
        if niz_pozicija[i]==minimum:
            rezultat.append(i+1)
    return rezultat

genome=input("Unesite genom:")
niz=MinimumSkew(genome)
for el in niz:
    print(el,end=" ")
