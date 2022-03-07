def KmersFrequnecy(text,k):
    D=dict()
    for i in range(0,len(text)-k+1):
        tmp=text[i:(i+k)]
        try:
            D[tmp]=D[tmp]+1
        except KeyError:
            D[tmp]=1
    return D

def MostFrequent(text,k):
    D=KmersFrequnecy(text,k)
    maksimum=max(D.values())
    return D.fromkeys([x[0] for x in D.items() if x[1]==maksimum],maksimum)

text=input("Unesite text: ")
k=int(input("Unesite k: "))
D=MostFrequent(text,k)
for x in D.items():
    print(x[0])
