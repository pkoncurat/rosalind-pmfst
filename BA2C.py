def Vjerojatnost(pattern,Profile):
    umnozak=1
    for i in range(len(pattern)):
        if pattern[i]=="A":
            vjerojatnost=Profile[0][i]
        elif pattern[i]=="C":
            vjerojatnost=Profile[1][i]
        elif pattern[i]=="G":
            vjerojatnost=Profile[2][i]
        elif pattern[i]=="T":
            vjerojatnost=Profile[3][i]
        umnozak*=vjerojatnost
    return umnozak
            


def ProfileProblem(text,k,Profile):
    D=dict()
    for i in range(0,len(text)-k+1):
        vjerojatnost=Vjerojatnost(text[i:(i+k)],Profile)
        try:
            D[text[i:(i+k)]]=vjerojatnost
        except KeyError:
            D[text[i:(i+k)]]=[vjerojatnost]
    maksimum=max(D.values())
    return D.fromkeys([x[0] for x in D.items() if x[1]==maksimum],maksimum)

if __name__ == "__main__":
    with open("../Downloads/rosalind_ba2c.txt", "r") as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
        Profile =[[float(l) for l in line.strip().split()] for line in f]
    D=ProfileProblem(text,k,Profile)
    for x in D.items():
        print(x[0])
