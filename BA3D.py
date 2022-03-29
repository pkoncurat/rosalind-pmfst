def DeBruijn(k,text):
    D=dict()
    for i in range(0,len(text)-k+1):
        if text[i:(i+k-1)] not in D.keys():
            D[text[i:(i+k-1)]]=text[(i+1):(i+k)]
        else:
            D[text[i:(i+k-1)]]+=","+text[(i+1):(i+k)]
    return D      

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3d.txt","r") as f:
        k=int(f.readline().strip())
        text=f.readline().strip()
    D=DeBruijn(k,text)
    for key in sorted(D.keys()):
        print(key+" -> "+D[key])
