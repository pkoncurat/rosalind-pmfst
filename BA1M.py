def NumberToSymbol(index):
    if index==0:
        return "A"
    elif index==1:
        return "C"
    elif index==2:
        return "G"
    elif index==3:
        return "T"

def Quotient(n,m):
    return n//m

def Reminder(n,m):
    return n%m

def NumberToPattern(index,k):
    if k==1:
        return NumberToSymbol(index)
    prefixIndex=Quotient(index,4)
    r=Reminder(index,4)
    symbol=NumberToSymbol(r)
    PrefixPattern=NumberToPattern(prefixIndex,k-1)
    return PrefixPattern+symbol
    

index=int(input("Unesite index:"))
k=int(input("Unesite k:"))
string=NumberToPattern(index,k)
print(string)
