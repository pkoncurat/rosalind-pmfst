def CountingPeptides(m,mase):
    broj_peptida={}
    for i in range(57):
        broj_peptida[i]=0

    for masa in range(55,m+1):
        broj_peptida[masa]=mase.count(masa)
        for int_masa in mase:
            if masa>=int_masa:
                if broj_peptida[masa-int_masa]>0:
                    broj_peptida[masa]+=broj_peptida[masa-int_masa]

    return broj_peptida[masa]

mase=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
print(CountingPeptides(1308,mase))#1308 je dana masa iz dataseta

    
