def ManhattanTouristProblem(n,m,Down,Right):
    s=[[0 for j in range(0,m+1)] for i in range(0,n+1)]#matrica tipa (n+1)*(m+1) popunjena nulama
    for i in range(1,n+1):
        s[i][0]=s[i-1][0]+Down[i-1][0]
    for j in range(1,m+1):
        s[0][j]=s[0][j-1]+Right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j]=max(s[i-1][j]+Down[i-1][j],s[i][j-1]+Right[i][j-1])
    return s[n][m]

if __name__=="__main__":
    with open("../Downloads/rosalind_ba5b.txt","r") as f:
        n,m=map(int,f.readline().strip().split())
        Down=[]
        for i in range(n):
            Down.append(list(map(int,f.readline().strip().split())))
        f.readline()   
        Right=[]
        for i in range(n+1):
            Right.append(list(map(int,f.readline().strip().split())))

    print(ManhattanTouristProblem(n,m,Down,Right))
    

