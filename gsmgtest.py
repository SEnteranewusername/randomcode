nnn=115792089237316195423570985008687907852837564279074904382605163141518161494337
from bitcoin import *
ccc = open("maximilianos.txt", 'w')
def revwordstring(rowhexstr):
 split_strings = []
 n=2
 for index in range(0, len(rowhexstr), n):
     split_strings.append(rowhexstr[index : index + n])
     byterevdone=''.join(reversed(split_strings))
 return (byterevdone)
def sha256utf(string):
    return(hashlib.sha256((string).encode('utf-8')).hexdigest())
def fpow():
    a=1
    b=[]
    while a<130:
        b=b+[(pow(a,nnn-2,nnn))]
        a=a+1
    return(b)
def htoinrow(needle):
    needle=needle.strip()
    rev= (str(needle))[::-1]
    revwordstringrevhex=revwordstring(needle)
    revwordstringhexrev=revwordstring(rev)
    fe=[rev,revwordstringrevhex,revwordstringhexrev,needle]
    allnume=[]
    for i in fe:
        i=int(i,16)
        a=i
        b=int((str(i))[::-1])
        c=nnn-i
        d=pow(i,nnn-2,nnn)
        allnume=allnume+[a,b,c,d]
    return(allnume)
def adm(num):
    a=1
    b=fpow()
    listnum=[]
    while a<129:
        n1=(a+num)%nnn
        n2=(a*num)%nnn
        n3=(num-a)%nnn
        n4=(a-num)%nnn
        n5=(num*b[a])%nnn
        a=a+1
        listnum=[n1,n2,n3,n4,n5]
    return(listnum)
def admpe(a,num):
        n1=(a+num)%nnn
        n2=(a*num)%nnn
        n3=(num-a)%nnn
        n4=(a-num)%nnn
        b=pow(a,nnn-2,nnn)
        n5=(num*b)%nnn
        listnum=[n1,n2,n3,n4,n5]
        return(listnum)

def convertp(num):
    hexnum=((hex(int(num)))[2:]).rjust(64,'0')
    hhexnum=(privtopub(hexnum))
    ccc.write(pubtoaddr(compress(hhexnum))+ '\n')
    ccc.write(pubtoaddr((hhexnum))+ '\n')
    ccc.write((hexnum)+ '\n')
    ccc.write((hhexnum[2:66])+ '\n')
##    return(hhexnum)
def convertp2(num):
##    hexnum=((hex(int(num)))[2:]).rjust(64,'0')
    hexnum=num.rjust(64,'0')
    hhexnum=(privtopub(hexnum))
    ccc.write(pubtoaddr(compress(hhexnum))+ '\n')
    ccc.write(pubtoaddr((hhexnum))+ '\n')
    ccc.write((hexnum)+ '\n')
    ccc.write((hhexnum[2:66])+ '\n')
    
def somevar(string):
    a=sha256utf(string)
    b=(string[2:66])
    c=(string[66:])
    e=sha256utf(b)
    f=sha256utf(c)
    all=[a,b,c,e,f]
    return(all)
def justhextoint(hexnu):
    return(int(hexnu,16))
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
 while isPrime(num,11)!=True:
     num=num+1
 #res=(hex(int(num)))[2:]    
 #c=(''.join(map(lambda x: chr(int(x,16)), [res[i:i+2] for i in range(0, len(res), 2)])))
 #convertp2(sha256utf(c))
 return(num)    
def undorime(num):
 while isPrime(num,11)!=True:
     num=num-1
 #res=(hex(int(num)))[2:]    
 #c=(''.join(map(lambda x: chr(int(x,16)), [res[i:i+2] for i in range(0, len(res), 2)])))
 #convertp2(sha256utf(c))
 return(num) 
def hex2ascii(num):
    hexa=hex(num)[2:]
    b=0
    xs=[]
    while len(hexa)>b:
        e=chr(int((hexa[b:(b+2)]),16))
        xs=xs+[e]
        b=b+2
    return(''.join(xs))
listforadd=['756e6b776f6e','554e4b574f4e','011101010110111001101011011101110110111101101110','010101010100111001001011010101110100111101001110','165156153167157156','125116113127117116','99928b9b9392','716663736766','208297e5c9673adfc7b6fea5ffdcfae3253103f5c0ea48ee30406c74e84c999d','d8ea856a6a70889538e10b540d34ba936b935066484024602e621ced3550ff77']
'''
with open("100bf45.txt") as f:
    for needle3d in f:
       for i in htoinrow(needle3d):
           for j in adm(i):
               for c in listforadd:
                  for n in admpe(j,justhextoint(c)):
                       me=convertp(n)
                       convertp(toprime(n))
                       for kaf in somevar(me):
                           convertp2(kaf)

with open("keyloltest3") as f:
    for needle3d in f:
       needle3d=(hex(int(needle3d.strip())))[2:] 
       for i in htoinrow(needle3d):
           for j in adm(i):
                       me=convertp(j)
##                       convertp(toprime(j))
                       for kaf in somevar(me):
                           convertp2(kaf)
'''
def brutemeed(string):
    b=fpow()
    for i in b:
        c=adm(i)
        for i in c:
            convertp(i)
            
def risen():
    c=[126,127,128]
    b=[]
    for i in c:
        b+=[(pow(i,nnn-2,nnn))]
    return(b)

def fastercal(e):
    d=[]
    c=-128
    while c<128:
            d+=[e+c]
            c+=1
    return(d)
 

from ecdsa import SigningKey, SECP256k1
from bitcoin import *
import csv
pcsvallh=open('categorylist.csv', 'a')
writers=csv.writer(pcsvallh)
def wrtier(a,b,c):
                cip=[str(a)]+[(str(b))]+[(str(c))]
                writers.writerow(cip)
                cipe=((" ".join(cip)))
                pcsvallh.write((cipe)+ '\n')
                ccc.write((a)+ '\n')
                ccc.write((b)+ '\n')
                
def keymaker(num):
    if num>0:
            num=num%nnn
##    try:
            sk=SigningKey.from_secret_exponent(num, curve=SECP256k1)
            vk=sk.verifying_key
            n1=((bin_hash160((vk.to_string("uncompressed")))).hex())
            n2=((bin_hash160((vk.to_string("compressed")))).hex())
            wrtier(n1,n2,num)
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

def sorting(string):
    string=[chr for chr in string]
    string.sort()
    return(''.join(string))
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
def strign(string):
    string=[chr for chr in string]
    return(string)
def updownse(string):
    string0=re.sub(r'[^0-9]','',string)
    a=(int(string0))-undorime(int(string0))
    c=toprime(int(string0))-(int(string0))
    b=((toprime(int(string0))-undorime(int(string0))))
    string=strign(string)
    return(digitalRootofbase(a,10),digitalRootofbase(c,10),string,b)
'''

with open('readme.txt','r') as file2:
 for ppp in file2:
  ze=ppp.split(" ")
  for line in ze:
    line=line.strip()
    #line=re.sub(r'[^0-9]','',line)
    try:
        ae=[line,line[::-1],sorting(line),sorting(line[::-1])]
        for zine in ae:
        
            a=''.join(dddon00(counter(re.sub(r'[^0-9]','',(base10Men310(line.lower()))))))[:78]
            b=str(toprime(int(a)))
            ne=[a,b,a[::-1],b[::-1]]
            for pine in ne:
                keymaker(int(pine))
##                keymaker(int((iandjreturn3(updownse(pine))),2))
    except:
        de=3

with open('readme.txt','r') as file2:
 for line0 in file2:
     ze=line0.split(" ")
  ##for line in ze:
  ##line=re.sub(r'[^0-9]','',line)
   
   ##try:
     ##ze=line0.split(" ")
     for line in ze:
        ae=[line,line[::-1],sorting(line),sorting(line[::-1])]
        for zine in ae:
            a=''.join((counter(re.sub(r'[^0-9]','',(base10Men310(line))))))[:78]
            b=re.sub(r'[^0-9]','',(base10Men310(line)))
            ne=[a,b,a[::-1],b[::-1]]
            for pine in ne:
                
                ##print((updownse(pine))[2])
                
                n=int((iandjreturn3(updownse(pine))),2)
                keymaker(n)
   #except:
        #fe=3
'''
#def keyextender():


def checkif(string):
    a=counter(string)
    k=0
    for i in a:
        
        if int(i)>5:
            k=1
    if k==0:
        return(a)
##ae='may there be prosperity for all.'
#3521034
#3151211013141
print('0110110101100001011110010010000001110100011010000110010101110010011001010010000001100010011001010010000001110000011100100110111101110011011100000110010101110010011010010111010001111001001000000110011001101111011100100010000001100001011011000110110000101110')
print(counter('0110110101100001011110010010000001110100011010000110010101110010011001010010000001100010011001010010000001110000011100100110111101110011011100000110010101110010011010010111010001111001001000000110011001101111011100100010000001100001011011000110110000101110'))
ae=[1, 2, 3, 6, 53, 106, 157, 159, 314, 318, 471, 942, 8321, 16267, 16642, 24963, 32534, 48801, 49926, 97602, 862151, 1724302, 2553919, 2586453, 5107838, 5172906, 7661757, 15323514, 135357707, 270715414, 406073121, 812146242]
be=[1, 2, 3, 6, 9, 18, 29, 58, 87, 174, 261, 522, 1555261, 3110522, 4665783, 9331566, 13997349, 27994698, 45102569, 90205138, 135307707, 270615414, 405923121, 811846242]
ce=[1, 2, 11, 22, 43, 86, 473, 946, 857977, 1715954, 9437747, 18875494, 36893011, 73786022, 405823121, 811646242]
aae=[1, 2, 103, 113, 139, 206, 226, 251, 278, 502, 11639, 14317, 15707, 23278, 25853, 28363, 28634, 31414, 34889, 51706, 56726, 69778, 1617821, 2921389, 3235642, 3593567, 3942457, 5842778, 7187134, 7884914, 406073071, 812146142]
abe=[1, 2, 16879, 24049, 33758, 48098, 405923071, 811846142]
ace=[1, 2, 3, 6, 19, 29, 38, 57, 58, 87, 97, 114, 174, 194, 291, 551, 582, 1102, 1653, 1843, 2531, 2813, 3306, 3686, 5062, 5529, 5626, 7593, 8439, 11058, 15186, 16878, 48089, 53447, 73399, 96178, 106894, 144267, 146798, 160341, 220197, 245507, 288534, 320682, 440394, 491014, 736521, 1394581, 1473042, 2789162, 4183743, 4664633, 7119703, 8367486, 9329266, 13993899, 14239406, 21359109, 27987798, 42718218, 135274357, 270548714, 405823071, 811646142]
def stringtonums(string):
    de=[]
    m=0
    while m<len(string):
        if int(string[m:m+4])<=2047:
            de+=[int(string[m:m+4])]
            m+=4
        elif int(string[m:m+4])>2047:
            de+=[int(string[m:m+3])]
            m+=3
    return(de,len(de))
def bip39finder(string):
    m=[]
    with open('englishbip.txt','r') as file2:
        for i in file2:
            m+=[i[:-1]]
    z=[]
##    string[0].sort()
    for b in string[0]:
        z+=[m[int(b)]]
    return(' '.join(z))
liste=[ae,be,ce,aae,abe,ace]
def sortalphabetical(string):
    string.sort(reverse=True)
    return(string)
def listobip39(string):        
 for i in liste:
    a=re.sub(r'[^0-9]','',(''.join(str(i))))
    if (stringtonums(a)[1])%12==0:
        print(' '.join(((bip39finder(stringtonums(a))))))
ew='1689414900598740054642660549463037697227265373243923344287830774191921152341700551605602806140371128510257827890558199490307580126'

def sumofwordinvanity(string):
    string=string.split(' ')
    #string=string.strip()
    z=0
    for i in string:
        z+=int(base10Men310(i.lower()))
    return(z)
def turnito(name):
    me=0
    with open(name,'r') as file2:
        
        for line in file2:
            me+=int(sumofwordinvanity((line.strip())))
        print(me)
turnito('nnny')
print((bip39finder(stringtonums(ew))))
def keysortalphabt(string):
    base='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    string=string.lower()+base
    m=''
    for i in string:
        if i not in m:
            m+=i
    return(m)
stri='A python sample snippet for reordering bipci mnemonic seed words into a valid bipci seed'
stri='corrects word order to fix checksum/compliance with bip39'
print(keysortalphabt(stri))
sa='1689414900598740054642660549463037697227265373243923344287830774191921152341700551605602806140371128510257827890558199490307580126'
print(sa[::-1])
print('##############')
'''
with open ('directpq','r') as file2:
    for line in file2:
        line=line.strip()
        print(base10Men310(line.lower()))
xx=1583916720
a=0

while a<602:
    #toprime
    #undorime
    if isPrime((xx-a),11):
        convertp((xx-a)*1476415299837939274529265729977723)
    if isPrime((xx+a),11):
        convertp((xx+a)*1476415299837939274529265729977723)
    a+=1
ccc.close()
pcsvallh.close()
'''
xx=1583916720
a=-602
ew=[]
while a<602:
    #if isPrime((xx+a),11)!=True:
    ew+=[(xx+a)]
    a+=1

#ew=[4488,4
def filetoarray(name):
    ew=[]
    with open(name,'r') as file:
        for line in file:
            ew+=[line]
    return(ew)
ew=filetoarray('moham1100')
#ew=['313','101']
'''
with open('pidigit','r') as file2:
    for line in file2:
        #print(len(line))
        for lz in ew:
            lz=lz.strip()
            if len(lz)>5:
                x = re.search(str(lz), line)
                if x!=None:
                    print((x),lz)
                    print(x.span()[0]) 
                x = re.search(str(lz[::-1]), line)
                if x!=None:
                    print((x),lz[::-1])

'''
def paiload():
    with open('pidigit','r') as file2:
        for line in file2:
            line=line.strip()
    return(line)

def euler2m():
    ms=''
    with open('phi','r') as file2:
        for line in file2:
            ms+=line.strip()
    return(ms)
onemilionpai=paiload()
eulernum2=euler2m()
def findwholePiore(lz,line):
    s,m,f=0,[],[]
    while s<1 and len(m)<100:
        x = re.search(str(lz), line)
        if x!=None:
                m+=[lz]
                lz=str(x.span()[0])    
        else:
            s=1
    return(m)    
#print(findwholePiore('110',onemilionpai))
def happy(num):
    b,e,nam=0,[num],0
    while int(num)>1 and b<100:
        bam=[chr for chr in str(num)]
        for i in bam:
            nam+=int(i)**2
        num,nam=nam,0
        if b>0 and str(num) in e:
            b=100
        else:    
            e+=[str(num)]
            b+=1
    return(e)
#it was for small number.
def aliq(num):
	a,b,c,d,f=0,(num+num%2)//2,[num],1,0
	while d>0 and f<100:
		while b>0:
			if num%b==0:
				a+=b
			b-=1
			f+=1
		if a not in c:
			num=a
			c+=[num]
			a=0
			b=(num+num%2)//2
    
		else:
			d=0
	return(c)
'''
with open('big.txt','r') as file2:
    for line in file2:
        #print(len(line))
        line=line.strip()
        mine=[line,line[::-1]]
        for i in mine:
           if len(i)>5: 
             a=(findwholePiore(i,onemilionpai))
             b=(findwholePiore(i,eulernum2))
             ne=happy(i)
             c=[a,b,ne]
             for j in c:
                 if len(j)>1:
                    #convertp(int(''.join(j))%nnn)
                    #convertp(int(''.join(j)[:78])%nnn)
                    xe=115792089237316195423570985008687907852837564279074904382605163141518161494336
                    if (int(''.join(j))%nnn) or (int(''.join(j)[:78])%nnn)==xe:
                        print(j)
                        print(line)
                     #print(j)
'''
#print(happy(1560))
#print(findwholePiore('786',eulernum2))
#print(findwholePiore('17',onemilionpai))
#print(aliq(75))
3ccc.close()