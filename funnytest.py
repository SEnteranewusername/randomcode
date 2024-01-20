import math
import random
import re
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
def numbertest(num):
    primelist=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021]
    z,p,q,n,s,nnn=[],[],[],0,0,1031
    a=range(1,1031)
    for i in a:
            f,m=1,0
            while f<1031:
                m+=f*i%nnn
                f+=1
            if i in primelist:
                p+=[m]
                n+=m//nnn
            else:
                q+=[m]
                s+=m//nnn
    print('n=',n,n//(len(primelist)))
    print('s=',s,s//(1031-len(primelist)))
    
    #print('q=',n)
    
        
#a=[1,3,4,5,6,7]
#b=map(a)
#numbertest(2)                
with open('steg','r') as file2:
    m,z,g=[],'',[]
    for line in file2:
        #for line in mine:
            #if 127<ord(mine) or(ord(mine))<32:
            m+=[[line,line[0],line[-1],len(line)]]
            z+=line
            g+=[line.split(' ')]
    m.sort(key=lambda x: x[3],reverse=True)
    z=[chr for chr in z]
    z.sort()
    
    #print(''.join(z))
    for line in g:
        #for mine in line:
        line.sort()
        #print(''.join(line))
            #mine.sort()
#idso,confirmed.
ae='''AB
ForProofsRangeZeroandfortotou^l


IOnePPedersen:
Torbenhadhaveinterestinginterviewsmostofthewaswith


CommitmentCommitment,InOverall,PedersenPedersenTorbenaaaaaandarticle,blindblindingcancommittedcreateddatagiveninisisitkeepofprivate.proofproverange.
sosomethingthatthatthethethethistototransactionusevaluevaluewaswaywewewhichwhowill


$30,000,$35,000$35,500,AForPorcheWell,Whyaaaaaccountaccountaccount,andapproachbankbankbeforeblindbutbuyingcarcar,costcouldcoulddoenoughenoughexample,forforforhadhadhashavehowififinininisknowmemightmoneymoneymoremuchneedneednotpaypayprivacy-awareproofproofproof.
provideprovideprovidepurchasesellersomeonesomething.something?thatthatthethethetheirtheytototototovalidvalue.wewerewhywithyouyouyouyouyouyouyouryour
Commitment
Pedersen


(g)(p(p,q,g,h)0CommitmentInPedersenTheThenZq,Z∗p.aaaandandandandarebecomescalculatecreatefromgeneratorh=g^s(modislargenumbersofofofoforderp).primepublicqq)ssecretsubgrouptakethethetotwovaluevaluesvalues.wewewewhich'''
ae=re.sub(r'[aeoiuy]','',ae)

def base10Men310(string):
    string=string.lower()
    a=['0 ',"1?!$^%/():&=,'.-_",'2abc','3def','4ghi','5jkl','6mno','7pqrs','8tuv','9wxyz']
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
def sert(string):
    z=''
    for i in string:
        if i.isupper():
            i='#'+i.lower()
        z+=i
    return(z)
zse='668#2668*81#46#687551#73776#73776#872663782051256325636426266883278338486677857377881773778764'
#for i in (base10Men310(sert(ae))):
'''
for mine in ae:
            if 127<ord(mine) or(ord(mine))<32:
                print(ord(mine),mine)
'''
#command and tor confirmed.
#base36confirmed
#png,steg confirm.
#color? probably. let test itn.---confirmed.--- logically its point to one finger based cryptographyu butwhy?
#in 45 min i could not get more,except the last thing i worked on before as data and etc which seem irrelvatn in hereor its better to say useless but proofable.
string='The Smallest Act Of Kindness Is Worth More Than The Grandest Intention.'.lower()

stre='The smallest act of kindness is worth more than the grandest intention.'

ae=re.sub(r'[Oscar Wilde]','',stre)
ae=re.sub(r'[^Oscar Wilde]','',stre)
print(ae)
#pi and e.
#8 44 33 1 7777 6 2 555 555 33 7777 8 1 2 222 8 1 666 333 1 55 444 66 3 66 33 7777 7777
#8431762553781228163154636377
#8431472633781468368466
#8 44 33 1 4 777 2 66 3 33 7777 8 1 444 66 8 33 66 8 444 666 66
#8 44 6 8 8 666 333 55 66 66 9 666 8 44 6 666 8 44 66 8 44 4 66 8 66 8 66 8 666 66 0
#33 1 7777 2 555 555 33 7777 1 2 222 1 444 3 33 7777 7777 1 444 7777 1 777 1 777 33 1 2 1 33 1 777 2 3 33 7777 1 444 33 444
#21 41 33 24 11 31 31 24 41 34 13 13 21 11 21 31 12 41 32 3
ste='33 1 7777 2 555 555 33 7777 1 2 222 1 444 3 33 7777 7777 1 444 7777 1 777 1 777 33 1 2 1 33 1 777 2 3 33 7777 1 444 33 444'
ste='8 44 6 8 8 666 333 55 66 66 9 666 8 44 6 666 8 44 66 8 44 4 66 8 66 8 66 8 666 66 0'
ste='8 44 33 1 7777 6 2 555 555 33 7777 8 1 2 222 8 1 666 333 1 55 444 66 3 66 33 7777 7777 1 444 7777 1 9 666 777 8 44 1 6 666 777 33 1 8 44 2 66 1 8 44 33 1 4 777 2 66 3 33 7777 8 1 444 66 8 33 66 8 444 666 66 0'
ste='8 44 33 1 7777 6 2 555 555 33 7777 8 1 2 222 8 1 666 333 1 55 444 66 3 66 33 7777 7777'
ste='33 1 7777 2 555 555 33 7777 1 2 222 1 444 3 33 7777 7777 1 444 7777 1 777 1 777 33 1 2 1 33 1 777 2 3 33 7777 1 444 33 444'
z,m=[],''
for i in ste.split():
    z+=[len(i)]
    m+=str(len(i))
print(len(z))
print(z[-2])
print(m)
ze=32
dd=['e','f','d','c']
'''
while ze<145:
    
    xe=hex(ze)[2:]
    if xe[0] and xe[1] not in dd:
        print(chr(ze))
        
    ze+=1
'''
#while
#The smallest act of kindness is worth more than the grandest intention.
aew=['"The smallest act',
'of kindness is worth' ,
'more than the',
'grandest intention."',
'_Oscar Wilde',]
listp=['13', '204', '3120', '6552', '7804', '20532', '137280', '123552', '1268088', '1302540']
def extracto(listkey,liststring):
    for i in listkey:
        i=[chr for chr in i]
        z=len(i)
        d=''
        for j in liststring:
            m,f=0,0
            while f<len(j):
                if (int(i[m%z])+f)<len(j):
                    d+=j[int(i[m%z])+f]
                    #print(d,int(i[m%z])+f)
                    f=int(i[m%z])+f
                    m+=1
                    
                    
                else:
                    f=len(j)
        print(d)
extracto(listp,aew)        