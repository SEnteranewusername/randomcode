number=4748748740111114778888520222144557788550011144112245570
def test(numb):
 d=[]
 while numb>1:   
    if numb%3==0:
        d+=['s']
        numb=numb//3
    elif numb%2==0:
        d+=['d']
        numb=numb//2
    elif numb%2==1:
        if numb%3==1:   
            d+=['m']
            numb=(numb-1)//6
        elif numb%3==2:
            d+=['i']
            numb=(numb+1)//6
 return(d)
def backto(string):
    z=1
    for i in string[::-1]:
        if i=='i':
            z=z*6-1
        elif i=='m':
            z=z*6+1
        elif i=='d':
            z=z*2
        elif i=='s':
            z=z*3
    return(z)
#print(hex(backto(test(number))))
#def reversefibo(number):
def fibo(string):
    while string>10000000000:
        string=string+string%2
        string=string-string//2
    print(string)
def stupidtest(string,numb):
   while string<=numb: 
        z=string
        string=string+string*2-string%2
   print(z)
   print(string)
#print(fibo(number))
#stupidtest(6654414317,number)
def feelgood(string):
    z=string+1
    while abs(z)>=abs(string) and string!=1:
        string=string+string%2
        string=string-string//2
        z=string
        
    print(z)
    print(string)

feelgood(number)
def testit(string):
    if string%3==0 and string%2==0:
        string=string-string//3-string//2
    elif string%3==0 and string%2==1:
        string=string-string//3
    elif string%3==0 and string%2==0:
        s=33
def shorter(string):
    d=[]
    while string>=1:
        n=23
        
        while n>1:
            if string==1:
                n=0
            elif string%n==0:
                string=string//n
                d+=['m']
                n=23
            elif string%n==1:
                string=string+1729
                d+=['a']
                n=23
    return(d)