def kSortingReversal(P,k):
    j=k
    while P[j]!=k+1 and P[j]!=-(k+1):
        j+=1
        
    P[k:(j+1)]=list(map(funkcija,P[k:(j+1)][::-1]))
    return P
        
    
def funkcija(x):
    return -x
    

def GreedySorting(P):
    for k in range(0,len(P)):
        if P[k]!=k+1:
            P=kSortingReversal(P,k)
            print("("+" ".join(["+"+str(el) if el>0 else str(el) for el in P])+")")
            if P[k]==-(k+1):
                P=kSortingReversal(P,k)
                print("("+" ".join(["+"+str(el) if el>0 else str(el) for el in P])+")")


if __name__=="__main__":
    with open("../Downloads/rosalind_ba6a.txt","r") as f:
        P=list(map(int,f.readline().strip().replace("(","").replace(")","").split()))
    GreedySorting(P)

