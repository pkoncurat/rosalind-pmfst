def GenomePathProblem(patterns):
    n=len(patterns)
    text=patterns[0]

    for i in range(1,n):
        text+=patterns[i][-1]

    return text

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3b.txt","r") as f:
        patterns=[line.strip() for line in f.readlines()]
    print(GenomePathProblem(patterns))   
