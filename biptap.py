from itertools import permutations
from bitcoin import *
nnn=115792089237316195423570985008687907852837564279074904382605163141518161494337
import hashlib
import numpy as np
def sha256utf(string):
    return(hashlib.sha256((string).encode('utf-8')).hexdigest())
def md5sha(string):
    return(hashlib.md5((string).encode('utf-8')).hexdigest())
import re
ccc = open("inputiii5.txt", 'a')
ddd = open("justcollectit", 'a')

def openfileaslist(name):
    lista=[]
    with open(name,'r') as file:
        for line in file:
            lista+=[line.strip()]
    return(lista)
def power(a, n, p):
     
    # Initialize result
    res = 1
     
    # Update 'a' if 'a' >= p
    a = a % p 
     
    while n > 0:
         
        # If n is odd, multiply
        # 'a' with result
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
             
            # n must be even now
            n = n // 2
             
    return res % p
     
# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def isPrime(n, k):
     
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
     
    # Try k times
    else:
        for i in range(k):
             
            # Pick a random number
            # in [2..n-2]     
            # Above corner cases make
            # sure that n > 4
            a = random.randint(2, n - 2)
             
            # Fermat's little theorem
            if power(a, n - 1, n) != 1:
                return False     
    return True

def dddon00(nes):
    a=[chr for chr in nes]
    while len(a)<=78:
        b=a[len(a)-1]
        c=len(a)-2
    
        g=0
        while c>-1:
                e=a[c]
        
                if b==e:
                    g=len(a)-1-c
                    c=-1
                elif b!=e:
                    c=c-1
                else:
                    g=0
        a=a+[str(g)]
    return(a)
def iandjreturn3(ds):
        j,k,s,b=int(ds[0]),int(ds[1]),(ds[2]),int(ds[3])
        n=0
        e=''
        z=''
        
        while n<256:
            f=(int(s[j-1])+int(s[k-1]))%b
            e=e+str(f%2)
            z+=str(f)
            s.append(f)
            s.pop(0)
            n=n+1
        return(''.join(e))
def sorting(string):
    string=[chr for chr in string]
    string.sort()
    return(''.join(string))
def counter(string):
##    string=re.sub(r"[^0-9]", "", string)
    d=''
    k=0
    n=0
    c=string[k]
    for i in string:
        n=n
        
        if i==c:
            n=n+1
        if i!=c:
            d=d+str(n)
            n=1
        if k==len(string)-1:
            d=d+str(n)
        
        k=k+1
        c=string[k-1]
##    counter(d)    
    return(d)
def alphfo(string,base):
    z=''
    for i in string:
        if i in base:
            z+=str(base.index(i))
    return(z)
lista=(openfileaslist('english.txt'))

def testitall(lista,allbase):
    for i in lista:
       
        manybaseroot(i)
        for j in allbase:
            ccc.write(str(alphfo(i,j))+ '\n')
            ccc.write(str(truebasecoverter(j,i))+ '\n')
        ccc.write(str(base10Men310(i))+ '\n')
def toprime(num):
 while isPrime(num,3)!=True:
     num=num+1
 return(num)    
def undorime(num):
 while isPrime(num,3)!=True:
     num=num-1
 return(num)
#tostring(lista,allbase)
def convertp(num):
    hexnum=((hex(int(num)))[2:]).rjust(64,'0')
    hhexnum=(privtopub(hexnum))
    ccc.write(pubtoaddr(compress(hhexnum))+ '\n')
    ccc.write(pubtoaddr((hhexnum))+ '\n')
    ccc.write((hexnum)+ '\n')
    ccc.write((hhexnum[2:66])+ '\n')
def testsimpleseed(string):
  #try:  
    a=str(int((iandjreturn3(updownse(string))),2))
    b=''.join(dddon00(str(string)))[:78]
   
    convertp(int(a)%nnn)
    convertp(int(b)%nnn)
  #except:
       #print(string)
      #aewe=43
def counter(string):
##    string=re.sub(r"[^0-9]", "", string)
    d=''
    k=0
    n=0
    c=string[k]
    for i in string:
        n=n
        
        if i==c:
            n=n+1
        if i!=c:
            d=d+str(n)
            n=1
        if k==len(string)-1:
            d=d+str(n)
        
        k=k+1
        c=string[k-1]
##    counter(d)    
    return(d)
def convertp2(num):
##    hexnum=((hex(int(num)))[2:]).rjust(64,'0')
    hexnum=num.rjust(64,'0')
    hhexnum=(privtopub(hexnum))
    ccc.write(pubtoaddr(compress(hhexnum))+ '\n')
    ccc.write(pubtoaddr((hhexnum))+ '\n')
    ccc.write((hexnum)+ '\n')
    ccc.write((hhexnum[2:66])+ '\n')
    #print(hexnum)
def taptapdcode(string,ms):
    if len(string)%2!=0:
        string='1'+string
    string=numseprator(string)
    
    for m in ms:
        z=''
        for i in string:
            z+=m[int(i[0])-1][int(i[1])-1]
        print(z)   
        f=sha256utf(z)    
        convertp2(f)
        convertp2((hex(toprime(int(f,16))))[2:])
        convertp2((hex(undorime(int(f,16))))[2:])
def findtruestring(n,j,keyfor):
  a=[n,j]
  for string in a:
    string=[chr for chr in string]
    m=''
    z=''
    se=''
    for i in string:
        if 1<int(i)<=5:
            m+=i
        if 1<int(i)<=8:
            z+=i
        if 1<int(i)<=6:
            se+=i
    #print(''.join(string))
    #print(z)
    if len(z)==len(string):
        ddd.write((z)+ '\n')
    if len(m)==len(string):
        taptapdcode(m,(rotateit(turntomatrix(keyfor))))
    if len(se)==len(string):
        print(se)

def keye(string):
    string=re.sub(r'[^a-z]','',string)+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    m=''
    for i in string:
        if i not in m:
            m+=i
    
    return(m[:-1])
def bipfastcheck():
    z=[]
    with open ('english.txt','r') as file2:
        for line in file2:
            line=re.sub(r'[^a-z]','',(line.strip()))
            
            line=md5sha(line)
            
            z+=[line]
    return(z)
def sometest(string,dict):
    keyfor=keye(string)
    string=string.split(' ')
    n=''
    j=''
    for b in string:
       
      if md5sha(b.strip()) in dict:
        i=md5sha(b.strip())
        n+=(np.binary_repr((dict.index(i)), width=11))
        j+=(np.binary_repr((dict.index(i))))
      elif md5sha(b[::-1].strip()) in dict:
        i=md5sha(b[::-1].strip())
        
        n+=(np.binary_repr((dict.index(i)), width=11))
        j+=(np.binary_repr((dict.index(i))))
      else:
          dse=2
    findtruestring(counter(n),counter(j),keyfor)
def openfileforbip39test(name):
    dict=bipfastcheck()
    with open(name,'r') as file3:
        k=0
        for line in file3:
          k+=1  
          try:  
            sometest(line.strip(),dict)
          except:
              print(k)
def rotatefortap(string):
    string=[chr for chr in string]
def turntomatrix(string):
    string=[chr for chr in string]
    z=[]
    n=0
    w=int((len(string))**0.5)
   
    while n<(len(string)):
        z+=[string[n:n+w]]
        n+=w
    return(z)
def rotateit(string):
    n=1
    z=[]
    while n<5:
        z+=[(np.rot90(string,n))]
        n+=1
    return(z)

def numseprator(string):
    k=0
    z=[]
    while k<len(string):
        z+=[string[k:k+2]]
        k+=2
    return(z)
def matrisall(base):
    z=(len(base))**0.5
def tapforall(string,base):
    for i in base:
        z=''
        for b in string:
            z+=i[int((b)[0])-1][int((b)[1])-1]
        ccc.write((z)+ '\n')
def taping(string):
    a=counter(string)
    if len(a)%2==0:
        n=[chr for chr in a]
        n.sort()
        if int(n[-1])==5:
            base='ABCDEFGHIJLMNOPQRSTUVWXYZ'[::-1]
            x=rotateit(turntomatrix(base))
            sepr=numseprator(a)
            tapforall(sepr,x)
        elif int(n[-1])==6:
            base='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[::-1]
            x=rotateit(turntomatrix(base))
            sepr=numseprator(a)
            tapforall(sepr,x)
        elif int(n[-1])==8:    
            base='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'[::-1]
            x=rotateit(turntomatrix(base))
            sepr=numseprator(a)
            tapforall(sepr,x)
'''
#openfileforbip39test('allposs.txt')
with open ('howo','r') as file2:
    for line in file2:
        #print(counter(line.strip()))
        taping(line[::-1].strip()) 
        #taping(np.binary_repr(int(line[::-1],16)))
        #taping(np.binary_repr(int(line,16)))
        #print((counter(line.strip())).sort())
'''        
#test=rotateit(turntomatrix('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#print(counter('00011011110101000101'))
ddd.close()
ccc.close()
print(isPrime(115792089237316195423570985008687907853269984665640564039457584007908834671663,3))
def fastmul():
    n=1
    a=3
    g=[]
    z=1
    while n<234:
        if isPrime(a,3):
            g+=[a]
            z=z*a
            n+=1
        a+=1
    print(g)
    print(z)
    print(toprime(z))
fastmul()