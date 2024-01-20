import re
def simpledict(name):
   a=[] 
   with open(name, 'r') as file1:
      #z=0 
      for line in file1:  
        needle1 = (line.strip()).lower()[::-1]
        #z+=1
        if len(needle1)>3:
            a+=[needle1]
   return(a)
def faster(name):
    z=''
    with open(name, 'r') as file1:
        for line in file1:
            z+=line.strip().replace(' ','').lower()
    return(z)
oeis=faster('names')
wordto=simpledict('dic')
def testarrange(fr,to):
    x=[]
    for i in fr:
        x+=[[len(re.findall(i,to)),i]]
    x.sort(key=lambda x: x[0],reverse=True)
    #x.sort(reverse=True)
    #print(x[0:10])
    return(x)
stre='The smallest act of kindness is worth more than the grandest intention oscar wilde'[::-1].lower().split(' ')
stre='''Elon Musk X elonmusk 168.4M+ igeaeamt followers No information is available for this page Learn why'''.lower().split(' ')
#for i in testarrange(stre,oeis):
#                print(i)
def openfile(name):
    namelist,ls=[],''
    with open(name,'r') as file:
        for line in file:
            ls+=line.strip().lower()
        
    ls.replace('  ',' ')
    for i in ls.split(' '):
       if i not in namelist:
           
           if len(i)>3:
            namelist+=[(re.sub(r'[^a-z]','',i))[::-1]]
    #ls=re.sub(r'[a-z]','',ls)    
    return(ls,namelist)
def doublecheck(name):
    filin=openfile(name)
    for i in testarrange(filin[1],oeis):
        print(i)
def numberco(string):
    d=[]
    for i in string:
        n=str(ord(i))
        z=0
        for p in n:
            z+=int(p)
        d+=[z]
    return(d)
print(numberco('No information is available for this page.'[::-1]))
a='xelnlw'.upper()
b='mlulgx'.upper()
print(numberco(b))
print(numberco(b[::-1]))
print(numberco(a))
print(numberco(a[::-1]))
a='موجودی کافی نیست'
b='موجودی کافی نمی باشد'
