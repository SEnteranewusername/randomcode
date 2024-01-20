import re

def allbasetogether():
    base85='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
    base85ea='''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstu'''
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
    
    casesen=[base12,base13,base62case,base58,base64,base69,base32case,base32normal,base32z,base32extend,base32geo,base31game,base36,base18,base26,base26par,base85ea,base85]
##    casesen=[base32case,base32normal,base32z,base32extend,base32geo]
    return(casesen)
def anotherway(lenst,string):
    p,e=0,0
    for i in string:
        conv=((len(string)-1)-e)
        e=e+1
##        ew=ew+str((i*lenst**conv))+' '
        p=p+(i*lenst**conv)
    #p=[chr for chr in str(p)]
    print(p)
##    print((hex(int(p)))[2:])
def stupidbaseconverter(basesource,string):
    for basesor in basesource:
        basec=[chr for chr in basesor]
        wr=[]
        fo=0
        fop=0
        e=0
        while e<len(string):
            if (string[e:e+1]) in basec:
                position = basec.index(str(string[e:e+1]))
                conv=((len(string)-1)-e)
                fo=fo+(position*len(basec)**conv)
                wr=wr+[(position)]
            e=e+1
        wick=[chr for chr in str(fo)]
        we=re.sub(r'[^0-9]','',str(wr))
        wee=re.sub(r'[^0-9]','',str(fo))
##        print((hex(int(we)))[2:])
##        print((hex(int(wee)))[2:])
        print(we)
        print(wee)
##        print(numlistbaserootcal((wr)))
        if len(string)!=len(wr):
           anotherway(len(basec),wr)
def wordsepration(bases,numstring):
    numstring=str(numstring)
    numstring=numstring.strip()
    for i in bases:
        i=i[::-1]
        c=len(i)-1
        e=0
        b=''
        while e<=(len((numstring))-1):
            if int(numstring[e:e+2])<=c:
                b=b+(i[int(numstring[e:e+2])])
                e=e+2
            else:    
##            if int(numstring[e:e+1])>c:
                b=b+(i[int(numstring[e:e+1])])
                e=e+1
                
        print(b)
      
with open("keylol") as f:
  for line  in f:
        needle=line.strip()
##    needle=str(int(needle,16))
##    needle=re.sub(r'[^0-9]','',str(needle))


##    needle=int(needle,16)
##        wordsepration(allbasetogether(),needle)
##        wordsepration(allbasetogether(),needle[::-1])
    
##        print(stupidbaseconverter(allbasetogether(),needle))
a='SHA256:MsMgGtDeitAEEe4fMns6sPVMfTyckqVR2fm5ZAd018s.'[::-1]
b='"/home/panther/.ssh/known_hosts" -R "5.161.147.134"'
c=0

a1=''
b1=''
dd=0
'''
while dd<16:
    c=0
    d=''
    b='"/home/panther/.ssh/known_hosts" -R "5.161.147.134"-------------------------------------'[dd:]
    for i in a:
      
        a1=a1+str(ord(i))+' '
        b1=b1+str(ord(b[c]))+' '
        d=d+chr((ord(i)-ord(b[c]))%127)+''
        c=c+1
        
    dd=dd+1
    
    print(d)
'''
##print(a1)
##print(b1)
##wordsepration(allbasetogether(),1259440144127475241)

def digitalRoot(num):
     
    # If num is 0.
    if (num == "0"):
        return 0
 
    # Count sum of digits under mod 9
    ans = 0
    for i in range (0, len(str(num))):
        ans = (ans + int(num[i])) % 5
         
 
    # If digit sum is multiple of 9, answer
    # 9, else remainder with 9.
    if(ans == 0):
        return 5
    else:
        return ans % 5
def digitalRootofbase(num,based):
     
    # If num is 0.
    if (num == "0"):
        return 0
 
    # Count sum of digits under mod 9
    ans = 0
    for i in range (0, len(str(num))):
        ans = (ans + int(num[i])) % based
         
 
    # If digit sum is multiple of 9, answer
    # 9, else remainder with 9.
    if(ans == 0):
        return based
    else:
        return ans % based
# Driver method
#num = "958"
def seprator(newo):
    rrw1=""
    a=0
    n2=0
    newo= (newo.split(" "))
    for line in newo:
        med=digitalRoot((line))
        rrw1=rrw1+str(med)
    return(rrw1)
def skipcipher(test_str):
    #liststringchar=test_str.split()
    liststringchar=[chr for chr in test_str]
    mex=1
    while mex<14:
        decodedstring=[]
        pose=-1
        for i in liststringchar:
            pose=pose+1
            if pose%mex==0:
            
            #if i==".":
            #if i.isalnum()==False:
                b=(liststringchar[(((pose)%(len(liststringchar))))])
                decodedstring=decodedstring+[b]
        print("".join(decodedstring))
        mex=mex+1
basec="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"

string=' یه چندوقته که دارم واسه خودم یه دنیای جدید میسازم. واسه خودم و تو. یه روزی از همین روزا میام دنبالت. دستتو میگیرم. میبرمت پیش خودم. اونجا جات امن تره. جام امن تره. فقط امیدوارم که آخرین نقشه‌ی فرارم خراب نشه. دعا کن نشه. دیگه چیزی نمونده. شب بخیر!'
#print(seprator(string))
def baseroot(string):
    
    de=''
    stringa=string.split(' ')
    for stre in stringa:
        e=0
        while e<len(stre):
            if (string[e:e+1]) in basec:
                position = basec.index(str(string[e:e+1]))
                de=de+str(position)+' '
            e=e+1
    print(de)
##baseroot(string)

##print(168**.5)
a=291700140302110350331130572004190311180471151406023003150331308061417042403120331160532037380418450
a=1331
b=13
def basetrueconverter(string):
    source='0123456789+_.'
    f,b=1,0
    e=''
    while source!=0:
        c=a%13**b
        source=string-c
        e+=source[c]
    return(e)
##base13='0123456789+_.'
##a='1337'
##basetrueconverter(a)
print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
needle='2772226744222232323222333232332322372232322222322323222332332772233232323332233322322237323332223232332223333333333333333333333333333333363233333333333333333333333333333333333333333333333333333333333337232333222332323232322232432333232323223222222233332422222379778227379778227737378223737627822637727822737942782243794278224372278222372278222862263622737237337236332223277232327732327797372373372363322232772323277323737336332223277232327727722377332833223333223322333232223333327322322332323333233332322377333232333332222232333323732333222323233222333333333333333333333333333333336323333333333333333333333333333333333333333333333333333333333333723233322233232323232223243233323232322322222223333242222297748277977482777374827376274827672748277942748274942748274227482722274827286226362273733633222327723232772773229343734223972232777277399983624983677248'
##wordsepration(allbasetogether(),needle)
##wordsepration(allbasetogether(),needle[::-1])
#print(basetrueconverter('115.665'))
base13='0123456789+_.'
base12='0123456789ab'
def truebasecoverter(base,string):
    m=0
    z=0
    for i in string[::-1]:
        m+=(base.index(i))*len(base)**z
        z+=1
    print(m)
truebasecoverter(base12,'4966465784572726723a2066973742069664657820675742066620726166765'[::-1])
##anotherway(base13,162440)
ewwww='https://aspb32.asset.aparat.com/aparat-video/3914195cebe8a24b29532b2be29162ca34373438-360p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjZmMjViMWMzOTJjYzIxZGRmZDFkYmEyYzE0MmE3ZjkwIiwiZXhwIjoxNjk5NzA1NzE1LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.p_cqxN78Jpl6ZmCV8hR2NxiMRYTaQGv5Guh-TDqSDI0'
m=''
'''
for i in ewwww:
    if i not in m:
        m+=i
#print(m)
'''
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
def truebaseconverter4(string):
    for i in allbasetogether():
        toupperbase(string,i)
'''
truebaseconverter('68719550089317649864481351249328938902756453')
truebaseconverter('68719550089317649864481351249328938902756453'[::-1]) 
##print(stupidbaseconverter(allbasetogether(),'68719550089317649864481351249328938902756453'))
wordsepration(allbasetogether(),'68719550089317649864481351249328938902756453')
wordsepration(allbasetogether(),'68719550089317649864481351249328938902756453'[::-1])
'''
#31462608203886812466491464062119951784639923780911362366430547309635559604189158256757321032322794568938408180603341709665748063598158814760930937602532216676
#10845561579384676
#79383037310019841833085992959
#68719550089317649864481351249328938902756453
def serwr(string):
    
        truebaseconverter(string)
        truebaseconverter(string[::-1]) 
##print(stupidbaseconverter(allbasetogether(),'68719550089317649864481351249328938902756453'))
        wordsepration(allbasetogether(),string)
        wordsepration(allbasetogether(),string[::-1])
def serwr2(string):
    
##        truebaseconverter(string)
##        truebaseconverter(string[::-1]) 
##print(stupidbaseconverter(allbasetogether(),'68719550089317649864481351249328938902756453'))
        wordsepration(allbasetogether(),string)
        wordsepration(allbasetogether(),string[::-1])
rerre='496e6465784572726f723a206c69737420696e646578206f7574206f662072616e6765'
print(re.sub(r'[cedf]','',rerre))
##serwr(str('434'))
s=int('4966465784572726723a2066973742069664657820675742066620726166765',16)
'''    print(hex('IndexError: list index out of range'))
TypeError: 'str' object cannot be interpreted as an integer'''
#serwr(str('45052235036552026845578406551595621553138347911634082468414260463696'))
print('$$$$$$$$$$$$$$$$$$$$$$')
def sterwer():
  with open ('salamefdl','r') as file2:
    for line in file2:
       try: 
        serwr(line.strip())
       except:
           ewr3=3
def stre(string,string2):
    k=0
    z=''
    for i in string:
       try: 
        z+=chr(abs(ord(i)-ord(string2[k])))
        
        k+=1
       except:
        k+=1   
    print(z)
##lowlevelsecms
##stre('lowlevelsecms','dosmeleniomdosme')
#66466871637724314618431774828315397
print('####################3')
base58='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
##truebasecoverter(base58,'196812261873184471724318615665187126919255381968156691843177482831539163012322873177482831539712731227422559122730017874647019681226125761566518719255387194841967371461843471774828315390123569127312133913926753716314683737846417243701')
#510237430825191857507550834203449025283598621334783813450916609258406994299
##toupperbase('196812261873184471724318615665187126919255381968156691843177482831539163012322873177482831539712731227422559122730017874647019681226125761566518719255387194841967371461843471774828315390123569127312133913926753716314683737846417243701',base58
base85='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
base64='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'

##base85no='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.\-:+=^!/*?&<>()[]{}@%$#'
base85ea='''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstu'''
sew='4d616e2069732064697374696e677569736865642c206e6f74206f6e6c792062792068697320726561736f6e2c2062757420627920746869732073696e67756c61722070617373696f6e2066726f6d206f7468657220616e696d616c732c2077686963682069732061206c757374206f6620746865206d696e642c20746861742062792061207065727365766572616e6365206f662064656c6967687420696e2074686520636f6e74696e75656420616e6420696e6465666174696761626c652067656e65726174696f6e206f66206b6e6f776c656467652c2065786365656473207468652073686f727420766568656d656e6365206f6620616e79206361726e616c20706c6561737572652e'
##toupperbase(str(int(sew,16)),base85ea)
print('testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
def correctpr(string):
    string=re.sub(r'[0O]','o',string)
    string1=re.sub(r'[Il]','i',string)
    string2=re.sub(r'[Il]','L',string)
    string3=re.sub(r'[Il]','1',string)
    string4=string.replace('I','i').replace('l','L')
    #return(string)
    (print(string1))
    (print(string2))
    (print(string3))
    (print(string4))
def cleantest58(name):
    base58='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    with open (name,'r') as file2:
        for line in file2:
           try:
               b=line.strip()
               
##               line=(correctpr(line))
               b=re.sub(r'[^123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]','',line)
##                line=line.strip()
##               print(b)
               print(truebasecoverter(base58,b))
               print(truebasecoverter(base58,b[::-1]))
##                line=int(line)
               #print(b,'len=',len(b))
##               print(b)
##               print(b[::-1])
##                print((hex(line))[2:])
               #serwr2(line)
           except:
               ds3=32
##            b=re.sub(r'[^123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]','',line)
##            truebasecoverter(base58,b)
##            truebasecoverter(base58,b[::-1])
#cleantest58('minew')
##print(hex(457882))
##print(truebasecoverter(base58,'sdserw'))
def keyroation(string):
    set='123456789'
    set1='789456123'
    set2='147258369'
    set3='963852741'
    set4='741852963'
    set5='987456321'
    set6='687954321'
    set7='687629153'
    setlist=[set1,set2,set3,set4,set5,set6,set7]
    k=[]
    for z in setlist:
        e=[]
        for i in string:
            e+=[z[set.index(i)]]
        k+=[''.join(e)]
    return(k)
with open ('moham119','r') as file2:
    for line in file2:
        line=line.strip()[::-1]
        eew=keyroation(line)
        for line222 in eew:
            print(line222)