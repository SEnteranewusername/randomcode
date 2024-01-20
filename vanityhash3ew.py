from itertools import permutations
from bitcoin import *
nnn=115792089237316195423570985008687907852837564279074904382605163141518161494337
import hashlib
def md5sha(string):
    return(hashlib.md5((string).encode('utf-8')).hexdigest())
import re
ccc = open("inputiii.txt", 'a')
def openfileaslist(name):
    lista=[]
    with open(name,'r') as file:
        for line in file:
            lista+=[line.strip()]
    return(lista)
def permit(listin):
    d=[]
    perm = permutations(listin,2)
    for i in perm:
        
        d+=[''.join(i)]
    return(d)

def digitalRootofbase(num,based):
    if (num == "0"):
        return 0
    ans = 0
    for i in range (0, len(str(num))):
        ans = (ans + (int((str(num))[i]))) % based
    if(ans == 0):
        return based
    else:
        return ans % based
def base10Men310(string):
    string=string.lower()
    a=['0 ',"1?!%/:&=,'.-_",'2abc','3def','4ghi','5jkl','6mno','7pqrs','8tuv','9wxyz']
    string=[chr for chr in string]
    j=''
    for i in string:
        z=0
        
        while z<10:
            if i in a[z]:
                j=j+str(z)
                z=10
            z=z+1
            if z==10:
                j=j+str(i)
    return(j)

def allbasetogether():
    base62case='0123456789abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    base58='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    base64='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    base69='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-*<>|'
    base32case='23456789CFGHJMPQRVWXcfghjmpqrvwx'
    base32normal='ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
    base32z='YBNDRFG8EJKMCPQXOT1UWISZA345H769'
    base32extend='0123456789ABCDEFGHIJKLMNOPQRSTUV'
    base32geo='0123456789BCDEFGHJKMNPQRSTUVWXYZ'
    base31game='0123456789BCDFGHJKLMNPQRSTVWXYZ'
    base36='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base18='ABCDEFGHILMNOPRSTU'
    base26='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base26par='ZYXWVUTSRQPONMLKJIHGFEDCBA'
    base12='0123456789AB'
    base13='0123456789+_.'
    base85i='''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstu'''
    base862='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~.'
    base861='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.\-:+=^!/*?&<>()[]{}@%$#'
    casesen=[base861,base862,base85i,base12,base13,base62case,base58,base64,base69,base32case,base32normal,base32z,base32extend,base32geo,base31game,base36,base18,base26,base26par]
##    casesen=[base32case,base32normal,base32z,base32extend,base32geo]
    return(casesen)
def manybaseroot(string):
    n=5
    string=[chr for chr in string]
##    z=[]
    m=''
    while n<27:
        
        for i in string:
            m+=str(digitalRootofbase(ord(i),n))
            
        ccc.write(str(m)+ '\n')
        m=''
        n+=1
##    return(z)
def wordsepration(i,numstring):
        numstring=re.sub(r'[^0-9]','',(str(numstring).strip()))
        c=len(i)-1
        e=0
        b=''
        while e<=(len((numstring))-1):
            if int(numstring[e:e+2])<=c:
                b=b+(i[int(numstring[e:e+2])])
                e=e+2
                
            else:    
            #elif int(numstring[e:e+1])>c:
                b=b+(i[int(numstring[e:e+1])])
                e=e+1
                
                
        return(b)
base12='0123456789ab'
def makeitreadyforbase(base,string):
    z=''
    for i in string:
        if i in base:
            z+=i
    return(z)
def truebasecoverter(base,string):
    string=makeitreadyforbase(base,str(string))
    m=0
    z=0
    for i in string[::-1]:
        m+=(base.index(i))*len(base)**z
        z+=1
    return(m)
def toupperbase(string,base):
    
    string=makeitreadyforbase(base,str(string))
    string=re.sub(r'[^0-9]','',string)
    base=[chr for chr in base]
    a=''
    if len(string)>1:
        
        z=int(string)
        while z>=len(base):
            a+=base[z%(len(base))]
            z=(z//len(base))
        if z<len(base):
                a+=base[z]
        return(a[::-1])
def numconverter(string,key):
    a='123456789'
    key=keymaker(keymaker(key)+a)
    z=[key[:3],key[3:6],key[6:]]
    b=''
    for i in string:
        k=0
        while k<3:
            if i in z[k]:
                b+=str(k+1)
                k=1000
            k+=1
    return(b)
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
def toprime(num):
 while isPrime(num,3)!=True:
     num=num+1
 res=(hex(int(num)))[2:]    
 c=(''.join(map(lambda x: chr(int(x,16)), [res[i:i+2] for i in range(0, len(res), 2)])))
 convertp2(sha256utf(c))
 return(num)
numberlist=['16773632','4147404','16711422','16777215','20921036','4776862','15539236','0','1','5']
def tryit(string):
  n=5
  while n>=3:
    z=permutations(string,3)
    w=['+','-','*','+','-','*','+','-','*']
    m=permutations(w,2)
    for i in z:
      for j in m:  
        c=i[0]+j[0]+i[1]+j[1]+i[2]
##        if (isPrime(abs(eval(c)),3))==True:
        print(abs(eval(c)),end=',')
    n-=1

a='3f48cc'
y='fff200'
g='fefefe'
w='ffffff'
b='000000'
r= 'ed1c24'
##tryit(numberlist)
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
lista=(openfileaslist('New'))
allbase=allbasetogether()
def testitall(lista,allbase):
    for i in lista:
       
        manybaseroot(i)
        for j in allbase:
            ccc.write(str(alphfo(i,j))+ '\n')
            ccc.write(str(truebasecoverter(j,i))+ '\n')
        ccc.write(str(base10Men310(i))+ '\n')
        
            #ccc.write(str(zzz)+ '\n')
##testitall(lista,allbase)
def toprime(num):
 while isPrime(num,3)!=True:
     num=num+1
 return(num)    
def undorime(num):
 while isPrime(num,3)!=True:
     num=num-1
 return(num)
def updownse(string):
    string0=re.sub(r'[^0-9]','',string)
    a=(int(string0))-undorime(int(string0))
    c=toprime(int(string0))-(int(string0))
    b=((toprime(int(string0))-undorime(int(string0))))
    if b==0:
        b=5
    string=[chr for chr in string]
    return(digitalRootofbase(a,len(string)),digitalRootofbase(c,len(string)),string,b)
lista=openfileaslist('maximilian01.txt')
def tostring(lista,allbase):
    for i in lista:
        for j in allbase:
            ccc.write(str(wordsepration(j,i))+ '\n')
            ccc.write(str(toupperbase(i,j))+ '\n')
tostring(lista,allbase)
ae=[16773632, 4147404, 16711422, 16777215, 20921036, 4776862, 15539236, 0, 1, 5, 4209614, 69309035222120, 37632458, 29337650, 69309001674856, 4085194, 69567045162750, 69567011739906, 1162563969736148668416]
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
'''
with open('nosin.txt','r') as file2:
    for line in file2:
        line=line.strip()
        line=counter(line)
        testsimpleseed(str(line))
        testsimpleseed(str(line)[::-1])
'''    

line=(1583929380-602)
def keye(string):
    string=re.sub(r'[^a-z]','',string)
    al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    m=''
    for i in string:
        if i not in m:
            m+=i
    m=m+a
    return(m[:-1])
    
def sometest(string):
    keyfor=keye(string)
    string=string.split(' ')
    for i in string:
        name=md5sha(i)
    
ccc.close()