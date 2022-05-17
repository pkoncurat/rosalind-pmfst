from math import *

def DPchange(money,Coins):
    MinNumCoins=[0]
    for m in range(1,money+1):
        MinNumCoins.append(inf)
        for coin in Coins:
            if m>=coin:
                if MinNumCoins[m-coin]+1<MinNumCoins[m]:
                    MinNumCoins[m]=MinNumCoins[m-coin]+1
    return MinNumCoins[money]
        

if __name__=="__main__":
    with open("../Downloads/rosalind_ba5a.txt","r") as f:
        money=int(f.readline().strip())
        Coins=[int(line) for line in f.readline().strip().split(",")]
    print(DPchange(money,Coins))
