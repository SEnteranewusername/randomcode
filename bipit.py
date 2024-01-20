with open('fast.txt') as f:
    haystacks = list(f)

with open('rfclittle.txt') as f:
    haystackss=[]
    n=0
    for line in f:
        needle = line.strip()
       
        
        for haystack in haystacks:
            if needle in haystack:
                n=n+1
                haystackss=haystackss+[needle]
                
    print (" ".join(haystackss))
    print(n)