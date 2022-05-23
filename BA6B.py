def NumberOfBreakpoints(P):
    br=0
    P.append(len(P)+1)
    P.insert(0,0)

    for i in range(0,len(P)-1):
        if P[i+1]-P[i]!=1:
            br+=1
    return br

if __name__=="__main__":
    with open("../Downloads/rosalind_ba6b.txt","r") as f:
        P=list(map(int,f.readline().strip().replace("(","").replace(")","").split()))
    print(NumberOfBreakpoints(P))
