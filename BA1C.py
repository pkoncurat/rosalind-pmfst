def Reverse(string):
    niz=[]
    for slovo in string:
        if slovo=="A":
            niz.append("T")
        if slovo=="C":
            niz.append("G")
        if slovo=="G":
            niz.append("C")
        if slovo=="T":
            niz.append("A")
    niz.reverse()
    novi_string=""
    for i in range(0,len(niz)):
        novi_string+=niz[i]
    return novi_string

string=input("Unesite pattern:")
novi_string=Reverse(string)
print(novi_string)
