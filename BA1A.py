def PatternCount(text,pattern):
    count=0
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:(i+len(pattern))]==pattern:
            count=count+1
    print(count)

text=input("Unesite text: ")
pattern=input("Unesite pattern: ")

PatternCount(text,pattern)
