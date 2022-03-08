def LastSymbol(pattern):
    niz=[]
    for slovo in pattern:
        niz.append(slovo)
    return niz[len(niz)-1]

def SymbolToNumber(symbol):
    if symbol=="A":
        return 0
    elif symbol=="C":
        return 1
    elif symbol=="G":
        return 2
    elif symbol=="T":
        return 3
    

def PatternToNumber(pattern):
    if pattern=="":
        return 0
    symbol=LastSymbol(pattern)
    prefix=pattern[0:len(pattern)-1]
    return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)

pattern=input("Unesite pattern:")
broj=PatternToNumber(pattern)
print(broj)
