from itertools import permutations
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
def gcdExtended(a, b):
 
    # Base Case
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y


def checkey(primelest,eulerlist):
    perm = permutations(primelest,2)
    xd='15165943121972409169171213758951813141543131412428154191312181219433121171617137149110916631213131281491109166131412199114371612126021664313711154112'
    matches=[]
    m=fileattack('maxi')
    for i in perm:
        c=i[0]*i[1]
        phi=(i[0]-1)*(i[1]-1)
        for b in eulerlist:
            if gcd(phi,int(b))==1:
                n=(gcdExtended(b,phi))[2]%phi
                #m=['151659431219724091691712137589518131415431314124281541913121812194331','21171617137149110916631213131281491109166131412199114371612126021664313711154112','1516594312197240916917121375895181314154313141242815419131218121943312','1171617137149110916631213131281491109166131412199114371612126021664313711154112','16894149005987400546426605494630376972272653732439233442878307741','91921152341700551605602806140371128510257827890558199490307580126','116894149005987400546426605494630376972272653732439233442878307741','191921152341700551605602806140371128510257827890558199490307580126']
                #m=[xd[0:len(str(c))-1],xd[::1][0:len(str(c))-1]]
                for j in m:
                  try:  
                    print(power(int(j[::-1]), n, c))
                  except:
                      new=2
primelist=[124907983,1904825461159416373,1476415299837939274529265729977723,7059975253980861700657068222131588590331,16417276400146549044608215201,10251280644094564100467271461,2882183671872152102506014320338942289199191]
eulerlist=[124907983,16773632,4147404,16711422,16777215,20921036,4776862,15539236,5,65537,13,11,14,]            
               
#pub=p*q
#aew=(encryptrsa(pub,e,m))
#print(aew)

#phi=(p-1)*(q-1)


#print(decryptionrsa(p,q,e,aew))

def fileattack(name):
    
    with open (name,'r') as file:
        m=[]
        for line in file:
            line=line.strip()
            m+=[line]
            m+=[line[::-1]]
        return(m)
wew='1689414900598740054642660549463037697227265373243923344287830774191921152341700551605602806140371128510257827890558199490307580126'
checkey(primelist,eulerlist)
'''
Traceback (most recent call last):
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/rsa2.py", line 93, in <module>
    checkey(primelist,eulerlist)
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/rsa2.py", line 69, in checkey
    print(power(int(j[::-1]), n, c))
ValueError: invalid literal for int() with base 10: '5676616270266602475760287564669602473796602a3276272754875646694'
>>> '''