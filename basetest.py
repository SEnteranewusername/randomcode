#print(''.join(map(lambda x: chr(int(x,2)), [res[i:i+8] for i in range(0, len(res), 8)])))
ccc = open("decoded0.txt", 'w')
import numpy as np
def simpledict(name):
   a=[] 
   with open(name, 'r') as file1:
      for line in file1:  
        needle1 = (line.strip()).lower()
        if len(needle1)>3:
            a+=[needle1]
   return(a)
dicname=simpledict('dictionary2.txt')
def simpledickchecker(string,dictu):
    z,k,m,l=' ',1,[' ',],len(string)
    for i in dictu:
        if i in string:
            z+=i
            k+=1
            m+=[i]
    if len(m)>5 and (((len(z)*k))/(len(m)*l))>0.3:
        print('source= ',string,'word= ',' '.join(m),k,((len(z)*(len(string)))/(len(m)*k)))
        
class baseconverterbin:
    def __init__(self, base, string):
        self.base = base
        self.string = string
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
        casesen=[base12,base13,base62case,base58,base64,base69,base32case,base32normal,base32z,base32extend,base32geo,base31game,base36,base18,base26,base26par]
##    casesen=[base32case,base32normal,base32z,base32extend,base32geo]
        return(casesen)
    def numbercalculation(nase):
        n=len(nase)
        z=3
        while n>2**z:
            z+=1
        return(z)
    def frombase(string):
        bases=baseconverterbin.allbasetogether()
        for bn in bases:
            baseconverterbin.numbercalculation(bn)
    def cleanit(string,base):
        m=''
        for i in string:
            if i in base:
                m+=i
                
        return(m)
    def stringtobase(string):
        bases=baseconverterbin.allbasetogether()
        for bn in bases:
            
            zx=baseconverterbin.cleanit(string,bn)
            #print(zx)
            #print((''.join(map(lambda x: bn[(int(x,2)%len(bn))], [string[i:i+baseconverterbin.numbercalculation(bn)] for i in range(0, len(string),baseconverterbin.numbercalculation(bn) )]))))
            #ccc.write((str( (((''.join(map(lambda x: bn[(int(x,2)%len(bn))], [string[i:i+baseconverterbin.numbercalculation(bn)] for i in range(0, len(string),baseconverterbin.numbercalculation(bn) )])))).lower(),dicname)))+ '\n')
            #ccc.write((str( (((''.join(map(lambda x: (bn[::-1])[(int(x,2)%len(bn))], [string[i:i+baseconverterbin.numbercalculation(bn)] for i in range(0, len(string),baseconverterbin.numbercalculation(bn) )])))).lower(),dicname)))+ '\n')
            ccc.write(''.join(map(lambda x: np.binary_repr(bn.index(x),baseconverterbin.numbercalculation(bn)), [zx[i:i+1] for i in range(0, len(zx),1 )]))+ '\n')
            ccc.write(''.join(map(lambda x: np.binary_repr(bn.index(x),baseconverterbin.numbercalculation(bn)), [(zx[::-1])[i:i+1] for i in range(0, len(zx),1 )]))+ '\n')

            #simpledickchecker(((''.join(map(lambda x: bn[(int(x,2)%len(bn))], [string[i:i+baseconverterbin.numbercalculation(bn)] for i in range(0, len(string),baseconverterbin.numbercalculation(bn) )])))).lower(),dicname)
            #print((''.join(map(lambda x: string[(int(x,2)%len(string))], [string[i:i+baseconverterbin.numbercalculation(bn)] for i in range(0, len(string),baseconverterbin.numbercalculation(bn) )]))))
#bin='011100100110100101101110011001110111010001101111011000100110000101110011011001010010100001110011011001010110110001100110001010010011101000001010001000000010000000100000001000000010000000100000001000000010000001100010011000010111001101100101011100110011110101100001011011000110110001100010011000010111001101100101011101000110111101100111011001010111010001101000011001010111001000101000001010010000101000100000001000000010000000100000001000000010000000100000001000000110011001101111011100100010000001100010011011100010000001101001011011100010000001100010011000010111001101100101011100110011101000100000000010100010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000110111001110101011011010110001001100101011100100110001101100001011011000110001101110101011011000110000101110100'
def converterfromhex():
  with open('keytest','r') as file2:
    for line in file2:
        #baseconverterbin.stringtobase((np.binary_repr((int(line[::-1],16)))))
        #baseconverterbin.stringtobase((np.binary_repr((int(line,16)))))
        baseconverterbin.stringtobase(line.strip())
        baseconverterbin.stringtobase(line[::-1].strip())
#a.stringtobase()
converterfromhex()
ccc.close()