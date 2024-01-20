
'''
ucita2_ltrs2ascii32 = {
	[0x00] = '\0',	[0x01] = 'E',	[0x02] = '\n',	[0x03] = 'A',	[0x04] = ' ',
	[0x05] = 'S',	[0x06] = 'I',	[0x07] = 'U',	[0x08] = '\r',	[0x09] = 'D',
	[0x0a] = 'R',	[0x0b] = 'J',	[0x0c] = 'N',	[0x0d] = 'F',	[0x0e] = 'C',
	[0x0f] = 'K',	[0x10] = 'T',	[0x11] = 'Z',	[0x12] = 'L',	[0x13] = 'W',
	[0x14] = 'H',	[0x15] = 'Y',	[0x16] = 'P',	[0x17] = 'Q',	[0x18] = 'O',
	[0x19] = 'B',	[0x1a] = 'G',	[0x1c] = 'M',	[0x1d] = 'X',	[0x1e] = 'V'
};

uucita2_figs2ascii32 = {
	[0x00] = '\0',	[0x01] = '3',	[0x02] = '\n',	[0x03] = '-',	[0x04] = ' ',
	[0x05] = '\'',	[0x06] = '8',	[0x07] = '7',	[0x08] = '\r',	[0x09] = 0x05,
	[0x0a] = '4',	[0x0b] = '\a',	[0x0c] = ',',	[0x0d] = '!',	[0x0e] = ':',
	[0x0f] = '(',	[0x10] = '5',	[0x11] = '+',	[0x12] = ')',	[0x13] = '2',
	[0x14] = '$',	[0x15] = '6',	[0x16] = '0',	[0x17] = '1',	[0x18] = '9',
	[0x19] = '?',	[0x1a] = '&',	[0x1c] = '.',	[0x1d] = '/',	[0x1e] = ';'
};

ITA2Charita2_ascii128 = {
	['\0'] = {'\0', FIGS},	['3'] = {0x01, FIGS},	['\n'] = {0x02, FIGS},
	['-'] = {0x03, FIGS},	[' '] = {0x04, FIGS},	['\''] = {0x05, FIGS},
	['8'] = {0x06, FIGS},	['7'] = {'\a', FIGS},	['\r'] = {0x08, FIGS},
	[0x05] = {0x09, FIGS},	['4'] = {'\n', FIGS},	['\a'] = {0x0b, FIGS},
	[','] = {0x0c, FIGS},	['!'] = {'\r', FIGS},	[':'] = {0x0e, FIGS},
	['('] = {0x0f, FIGS},	['5'] = {0x10, FIGS},	['+'] = {0x11, FIGS},
	[')'] = {0x12, FIGS},	['2'] = {0x13, FIGS},	['$'] = {0x14, FIGS},
	['6'] = {0x15, FIGS},	['0'] = {0x16, FIGS},	['1'] = {0x17, FIGS},
	['9'] = {0x18, FIGS},	['?'] = {0x19, FIGS},	['&'] = {0x1a, FIGS},
	['.'] = {0x1c, FIGS},	['/'] = {0x1d, FIGS},	[';'] = {0x1e, FIGS},
	['\0'] = {'\0', LTRS},	['E'] = {0x01, LTRS},	['\n'] = {0x02, LTRS},
	['A'] = {0x03, LTRS},	[' '] = {0x04, LTRS},	['S'] = {0x05, LTRS},
	['I'] = {0x06, LTRS},	['U'] = {'\a', LTRS},	['\r'] = {0x08, LTRS},
	['D'] = {0x09, LTRS},	['R'] = {'\n', LTRS},	['J'] = {0x0b, LTRS},
	['N'] = {0x0c, LTRS},	['F'] = {'\r', LTRS},	['C'] = {0x0e, LTRS},
	['K'] = {0x0f, LTRS},	['T'] = {0x10, LTRS},	['Z'] = {0x11, LTRS},
	['L'] = {0x12, LTRS},	['W'] = {0x13, LTRS},	['H'] = {0x14, LTRS},
	['Y'] = {0x15, LTRS},	['P'] = {0x16, LTRS},	['Q'] = {0x17, LTRS},
	['O'] = {0x18, LTRS},	['B'] = {0x19, LTRS},	['G'] = {0x1a, LTRS},
	['M'] = {0x1c, LTRS},	['X'] = {0x1d, LTRS},	['V'] = {0x1e, LTRS}
};
'''

def openfileandread(name):
   a=[]
   z=''
   with open(name, 'r') as file1:  
     for line in file1:
          needle1 = (line.strip())
          needle2=needle1.split('–')
          if len(needle2)>1:
              a=a+[str(needle2[0]).replace(' ','')]+[str(needle2[1])]
              z+=str([str(needle2[0]).replace(' ','')])
            
##   print(re.sub(r'[^a-z]','',z))
   return(a)
def osie(name):
   a=[]
   z=''
   with open(name, 'r') as file1:  
     for line in file1:
          needle1 = (line.strip())
          needle2=needle1.split('–')
          if len(needle2)>1:
              a=a+[str(needle2[0]).replace(' ','')]+[str(needle2[1])]
              z+=str([str(needle2[0]).replace(' ','')])
            
##   print(re.sub(r'[^a-z]','',z))
   return(a)
dicname='cleanfile'
##dicname='abstract'
dic=(openfileandread(dicname))
def dictest(string):
    
    #dic=(openfileandread(dicname))
    k,z,n,x,fe=0,'',0,len(string),0
    evaluato=''
    info=[]
    for i in dic:
        if k%2==0:
            if i in string:
                evaluato+=i+','
                info=info+[str(i),str(dic[k+1])]
                z=z+i
                n+=1
                fe+=(len(i)**2)
        k+=1        
        if k==len(dic):
            x=((len(z)+fe))/len(string)*n
            if n>1 and x>0:
                print(x,evaluato,info)
                print(string)

def simpledict(name):
   a=[] 
   with open(name, 'r') as file1:
      for line in file1:  
        needle1 = (line.strip()).lower()
        if len(needle1)>3:
            a+=[needle1]
   return(a)
def stringtocheck(name):
    with open(name, 'r') as file1:
      for line in file1:  
        needle1 = (line.strip())
        fix=(re.sub(r'^[a-zAZ]','',needle1)).lower()
        dictest(fix)
        dictest(fix[::-1])
def simpledickchecker(string,dictu):
    z,k,m,l=' ',1,[' ',],len(string)
    for i in dictu:
        if i in string:
            z+=i
            k+=1
            m+=[i]
    if len(m)>7 and (((len(z)*k))/(len(m)*l))>0.50:
        print('source= ',string,'word= ',' '.join(m),k,((len(z)*(len(string)))/(len(m)*k)))
def filecheck(name,dictr):
    dictu=simpledict(dictr)
    with open(name,'r') as file11:
        for line in file11:
            line=(re.sub(r'^[a-zAZ]','',line)).lower()
            simpledickchecker(line,dictu)
            simpledickchecker(line[::-1],dictu)
##filecheck('Newewe','newdic.txt')    
dicname=simpledict('dictionary.txt')
#dicname=simpledict('abstract')
##a='profbillbuchananobe'[::-1]
a='''Range Proofs For Zero to u^l and for A to B?'''
b='''Range Proofs For Zero to u^l and for A to B?'''[::-1]
a='Why might me need to blind a value. Well, why do we need to know how much someone has in their bank account before they purchase something? A more privacy-aware approach is to provide proof that you have enough money to pay for something. For example, if you were buying a Porche for $30,000, and you had $35,000 in your bank account, you could provide the seller with a proof that you had enough money in your account to pay for the car, but if the car cost $35,500, you could not provide a valid proof.'.replace(' ','').lower()
b='Why might me need to blind a value. Well, why do we need to know how much someone has in their bank account before they purchase something? A more privacy-aware approach is to provide proof that you have enough money to pay for something. For example, if you were buying a Porche for $30,000, and you had $35,000 in your bank account, you could provide the seller with a proof that you had enough money in your account to pay for the car, but if the car cost $35,500, you could not provide a valid proof.'[::-1]
b=a[::-1]
a='(g)(p(p,q,g,h)0CommitmentInPedersenTheThenZq,Z∗p.aaaandandandandarebecomescalculatecreatefromgeneratorh=g^s(modislargenumbersofofofoforderp).primepublicqq)ssecretsubgrouptakethethetotwovaluevaluesvalues.wewewewhich'.lower()
dictest(a)
dictest(a[::-1])

##filefortestname='textotest'
##stringtocheck(filefortestname)          
##(openfileandread(dicname))             
       
##print(dic[12])
##string='This website uses cookies to help it function properly. These cookies are used to optimise and customise your customer-experience. Should you continue using this website, then we assume that you are okay with that.'

with open('testfile','r') as file2:
    for i in file2:
        simpledickchecker(i.lower(),dicname)
        #dictest(i[::-1].lower())
