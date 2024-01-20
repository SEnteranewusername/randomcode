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
#onemilionpai=paiload()
#eulernum2=euler2m()
#eee=eee()
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
#print(findwholePiore('13109',eulernum2))
#print(findwholePiore('13109',onemilionpai))
#print(aliq(75))
#ccc.close()

def toupperbase(string,base):
    base=[chr for chr in base]
    a=''
    z=int(string)
    while z>len(base):
        a+=base[z%(len(base))]
        z=(z//len(base))
    if z<=len(base):
            a+=base[z]
    print(a[::-1])
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
test='fecfbafbbfbcfebfe'
base='0123456'
#aaa=str(truebasecoverter(pkeyconverter(test),base))

#print(findwholePiore(aaa,eulernum2))
#print(findwholePiore(aaa,onemilionpai))
#base12, is it a trap or what? let try that. no. yes. wait. just do it.
#hamkhan confirmed for pearson.
#2882183671872152102506014320338942289199191
#07059975253980861700657068222131588590331
#16417276400146549044608215201
#10251280644094564100467271461
#1476415299837939274529265729977723
#1904825461159416373
#its irrational if we look for brail music notation? why? the kor group or koor group? hamkhan fucking.
#fucking chimistry and electronic are here too! yet as im fucking care about the person whom might be might be that person and this whole shit could not be just a trick as its seem then i should fucking cooaporate. its so fuckingfunny.
#and i should ignore fucking russian word in here too. why? because its might be true where its should or could seem funny for some whom made other to communicate with this method.
'''
with open('paxi','r') as file2:
    for line in file2:
        line=line.strip()[::-1]
        try:
            if len(line)>6 and isPrime(int(line),11)==True:
                er=3
                #print(line)
        except:
            ew=2



        if len(line)>6:
            ze=[(findwholePiore(line,eulernum2)),(findwholePiore(line,onemilionpai)), (findwholePiore(line,eee))]
            for mine in ze:
                if len(mine)>0:
                    print(mine)
           
'''
file2check=['Euler.txt','sqrt2.txt','sqrt3.txt','Ee.txt','gr.txt','Pi16.txt','log2.txt','log10.txt','Le.txt','Ga.txt','Ca.txt']
def checkwholelist(listname,listnum):
    for i in listname:
        file=''
        with open (i,'r') as tot:
            z=0
            for line in tot:
               if z<1:  
                   line=str('0')+line.strip().split('.')[1]
                   z+=1
                   file+=line
               else:
                   file+=line
            #file=file.split('.')
            #file=str(0)+file[1]
            for g in listnum:
                if len(g)>3:
                    if g in file:
                        #print(g,i)
                        #ccc.write((i)+ '\n')
                        #ccc.write((g)+ '\n')
                        print(findwholePiore(file,g))
def fileopen(name):
    with open(name,'r') as file:
        x=[]
        for line in file:
            line=line.strip()
            x+=[line]
        return(x)
#file2check=['Newrer']
def fileditor(listname):
    for i in listname:
        with open(i,'r') as file:
            big=''
            for line in file:
                line=line.strip()
                big+=line
            j=re.search('\.', big)
            ddd = open('1'+i, 'w')
            ddd.write(big[(j.span()[0]):])
            
            file.close()
            ddd.close()
fileditor(file2check)
#checkwholelist(file2check,fileopen('checkitnow'))
#a='324443434356546423232455454522434312'
#print(re.search('24',a))
ccc.close()
#['26111932', '28872013']
#['23911162', '4116333', '2915111', '6457040', '16802989']
#['13696214', '33341933']
#['7429001', '6548806', '3893177', '3551909', '19638204', '1187646', '912463', '1484384', '47675444']