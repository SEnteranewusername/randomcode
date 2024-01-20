nnn=115792089237316195423570985008687907852837564279074904382605163141518161494337
#from bitcoin import *
ccc = open("outputn.txt", 'a')

import re
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
def isPrime(n, k):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):
            a = random.randint(2, n - 2)
            if power(a, n - 1, n) != 1:
                return False     
    return True
def toprime(num):
 while isPrime(num,11)!=True:
     num=num+1
 return(num)    
def undorime(num):
 while isPrime(num,11)!=True:
     num=num-1
 return(num) 

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
def eee():
    ms=''
    with open('Ee.txt','r') as file2:
        for line in file2:
            ms+=line.strip()
    return(ms)
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
    return(e).
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
def pkeyconverter(string):
    a='cdefgab'
    b='1234567'#base9999
    z=''
    for i in string:
        z+=str(a.index(i))
    return(z)
def truebasecoverter(string,base):
    m=0
    z=0
    for i in string[::-1]:
        m+=(base.index(i))*len(base)**z
        z+=1
    return(m)
file2check=['Euler.txt','sqrt2.txt','sqrt3.txt','Ee.txt','gr.txt','Pi16.txt','log2.txt','log10.txt','Le.txt','Ga.txt','Ca.txt']
def checkwholelist(listname,listnum):
    for i in listname:
        file=''
        with open (i,'r') as tot:
            for line in tot:
               line=line.strip()
               file+=line
            
            for g in listnum:
                if len(g)>8:
                    if g in file:
                        #print(g,i)
                        ccc.write((i)+ '\n')
                        ccc.write((g)+ '\n')
def fileopen(name):
    with open(name,'r') as file:
        x=[]
        for line in file:
            line=line.strip()
            x+=[line]
        return(x)
def superseedtest(string):
    z=len(string)
    
    
#a='324443434356546423232455454522434312'
#print(re.search('24',a))
ccc.close()
#['26111932', '28872013']
#['23911162', '4116333', '2915111', '6457040', '16802989']
#['13696214', '33341933']
#['7429001', '6548806', '3893177', '3551909', '19638204', '1187646', '912463', '1484384', '47675444']