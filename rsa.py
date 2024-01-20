def gcd(num,num1):
    d,p=num,num1
    while p>0:
        x=d%p
        d=p
        p=x
        if d==p:
            p=0
    return(d)
def power(a, n, p):
    res = 1
    a = a % p    
    while n > 0:
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2
    return res % p
def rsa(p,q,e):
    pub=p*q
    phi=(p-1)*(q-1)
    pv=pow(e,phi-2,phi)
    return(pub,pv)
def encryptrsa(pub,e,m):
    if len((str(m)))<pub:
        if m**e!=m**e%pub:
            return(m**e%pub)
    else:
        print('go to right padding')
def decryptionrsa(p,q,e,enc):
    pv=rsa(p,q,e)[1]
    pub=rsa(p,q,e)[0]
    #phi=(p-1)*(q-1)
    decrypti=power(enc,pv,pub)
    return(decrypti)

p=16417276400146549044608215201
q=10251280644094564100467271461
e=13
m=14577554887702558755447
pub=p*q
aew=(encryptrsa(pub,e,m))
print(aew)

phi=(p-1)*(q-1)

print(decryptionrsa(p,q,e,aew))


#aw=power(8,421,1031)
def invmod(m,n):
    g,f,p,q=0,1,0,1
    while q!=0:
        c,d=m//n,m%n
        p,q=n//c
    
    
    
    if gcd(m,n)==1:
        #c,b,x,f,k=m//n,(m+1)%n,gcd(n,b)
        c,b=(m+1)//n,(m+1)%n
        l=gcd(n,b)
        f=gcd(c,b)
        print(l)
        print(f)
        x=l//f+c//f
        print(x)
        #print('x',x)
        #print('f',f)
        print(x*n%m)
print(60*15%37)
#invmod(37,15)
b=313*311
ede=310*312
e=7
a=1
while (7*a)%ede!=1:
    a+=1
print('a',a)
ce=151**e%b
print(ce)
env=83437
few=82903
de=power(ce, env, b)
ge=power(ce, few, b)
print(ge)
print(gcd(41,15))
print(few**e%b)
'''        
        
        while (c*n%m)!=1:
            c+=1
    return(c)
print(invmod(120,7))
'''
print('###############################')
def extendgcd(a,b):
    s,t,f,g=1,a//b,0,1
    while f!=g or gcd(a,b)!=1:
        if a>b:
            x,r=b//a,b%a
            b,a=r,b
        if b>a:
            x,r=a//b,a%b
            b,a=r,b
        m,k=s,t    
        s,t,f,g=x*s-f,x*s-g,m,k
        print(s,t)
def extendgcdlist(a,b):
    s,t,k=[0,1],[1,0],1
    while a%b!=0 or gcd(a,b)!=1:
        if a<b:
            x,r=b//a,b%a
            b,a=r,b
        if b<a:
            x,r=a//b,a%b
            b,a=r,b
        k+=1  
        s+=[s[(k-1)]*x-s[k-2]]
        t+=[t[k-1]*x-t[k-2]]
        print(s,t)
def gcd2(num,num1):
    d,p=num,num1
    ce=[]
    while p>0:
        x=d%p
        ce+=[d//p,x]
        d=p
        p=x
        if d==p:
            p=0
    return(ce)
print(gcd2(38,15))

print(gcd(42,5))
print(extendgcdlist(42,5))
print(15*5-42*2)