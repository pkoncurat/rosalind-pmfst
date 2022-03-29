def OverlapGraph(patterns):
    for i in range(0,len(patterns)):
        for j in range(0,len(patterns)):
            if i!=j:
                if patterns[i][1:len(patterns[i])]==patterns[j][:len(patterns[j])-1]:
                    print(patterns[i]+" -> "+patterns[j])


if __name__ == '__main__':
    with open('../Downloads/rosalind_ba3c.txt', 'r') as f:
        patterns = [line.strip() for line in f.readlines()]
    OverlapGraph(patterns)              
