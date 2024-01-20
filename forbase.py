##from io import BytesIO
##from baudot import decode_to_str, codecs, handlers
from itertools import permutations
import re
def baseconverterstep0(string):
    string=string[::-1]
    b=0
    k=0
    for i in string:
        
        b=b+((int(i,16)))*12**k
        k=k+1
##        print(b)
        
       
    return(b)
##print(baseconverterstep0('12'))        
##    print(string.replace('b','$').replace('a','b').replace('$','a'))
def baseconverter(string):
##    string=[chr for chr in string]
    a='+-*/'
    b=[]
    k=0
    c=''
    while k<=(len(string)-1):
        c=c
        if string[k] not in a:
            c=c+(string[k])
        if string[k] in a:
            if len(c)>0:
                c=str(baseconverterstep0(c))
                b=b+[c]+[string[k]]
                c=''
            elif len(c)==0:
                b=b+[string[k]]
        if k==(len(string)-1):
           if len(c)>0:
                c=str(baseconverterstep0(c))
                b=b+[c]
                c=''
        k+=1
    a=(''.join(b))
    try:
        a=a.replace('/','//')
        print(eval(a))
        print((hex(int(eval(a))))[2:])
    except:
        ce=33
def base12c(string):
    string=[chr for chr in string]
    n=0
    b=[]
    c=''
    d=''
    while n<len(string)-1:
        e=int(string[n])
        f=int(string[n+1])
        b=b+[((e*12)/(f*12))]
        c=c+str(e)
        d=d+str(f)
        n=n+2
    print(b)
    print(c)
    print(d)
string='11441111443224441125243314112414461121242444111521112413163534441112464133352444351512223444182435114434113318242524331211223411114446252433123421221433'
string='121111123311111312113211113123111111121332113133111112123113131311341121411111312133131311341121211111231333311121131211121121131231341121213212'
base12c(string)
def replacer(string):
    return(string.replace('a','$').replace('b','a').replace('$','b'))


#base12('1411432412231121412224112121133411443324311234123143131222311231144223132213')


perm = permutations([1, 2, 3])
 # Print the obtained permutations
class numkeyfinder:
    def numbercombinationtolist(numlist):
        medio=[]
        perm = permutations(numlist)
        for i in list(perm):
            medio=medio+[i]
        return(medio)
    def vowelranker(string,numlist):
        a=numkeyfinder.numbercombinationtolist(numlist)
        vowel=['c','d','e','f']
        outlist=[]
        for i in a:
            res = string.replace('c', str(i[0])).replace('d',str(i[1])).replace('e',str(i[2])).replace('f',str(i[3]))
            outlist=outlist+[res]
        return(outlist)
'''
ae=[
'a1a8e2612a22b12213c1af3b714c147f174571471d263248194131e',
'1e19d75e71772e77e43e1b42fe03e0fbef08fe0fea754709e60e4ed',
'e1e6a4814e44014417f1ec70312f123c132631231d487426192171a',
'ede6af8dfeff7dffd04de207bdc4dcb2dbc9bdcbd1f80fc6d5cd0da',
    ]
for i in ae:
    d=(numkeyfinder.vowelranker(i,['+','-','/','*']))
    
    print(i)
    for c in d:
        print(c)
'''
def base12(string):
    a=['11','12','13','14', '21', '22', '23', '24', '31','32', '33', '34', '41','42', '43', '44']
    b='123a456b789ce0fd'
    c='e7410852f963dcba'
    d='147e2680369fabcd'
    e='df0ec987b654a321'
##    e='tabcwxyzdeftabcw'
    le0n=0
    bb=''
    cc=''
    dd=''
    ee=''
    while le0n<(len(string)):
        m=string[le0n:le0n+2]
        
        z=0
       
        while z<len(a):
            if a[z]==m:
                bb=bb+b[z]
                cc=cc+c[z]
                dd=dd+d[z]
                ee=ee+e[z]
                z=20
            z=z+1
        le0n=le0n+2
    ae=[bb,cc,dd,ee]
    for iii in ae:
        c002=(replacer(iii))
        c0021=(replacer(iii[::-1]))
        grand=[c002,iii,iii[::-1],c0021]
        for ggg in grand:
            vam=re.sub(r'[^0123456789ab]','',ggg)
            print(vam)
            print(ggg)
            dam=(numkeyfinder.vowelranker(str(ggg),['+','-','/','*']))
            for final in dam:
                baseconverter(final)
print('########################')
base12('4214133241131312441341313211121311241323')
base12('4214133241131312441341313211121311241323'[::-1])
base12('2141332411313124413413132111213112413231')
base12('2141332411313124413413132111213112413231'[::-1])
print('########################@@@@@@@@@@@@@@@@@@')
base12num='0123456789ab'
abjad = ["ابجد","هوز","حطی","کلمن","سعفص","قرشت","ثخذ","ضظغ"]
def searchifinarray1(text):
    fapointbin=["ابجد","هوز","حطی","کلمن","سعفص","قرشت","ثخذ","ضظغ",'0','1','4']
##    fapointbin=["ابجد","هوز","حطی","کلمن","سعفص","قرشت","ثخذ","ضظغ"]

    j=''
    n=''
    ew=''
    for i in text:
        k=0
        
        while k<len(fapointbin)-1:
            if i in fapointbin[k]:
              if k<8:  
                d=fapointbin[k]
                z=d.index(i)
                #j+=str(k+1)+str(z+1)
                j+=str(z+1)
                n+=str(k)
                ew+=str(k+1)
                k=1000
              elif (len(fapointbin)-1)>k>8:
                j+=str(fapointbin[k])+i
                k=11111
            
                
                
            k=k+1
    print(j)
    print(n)
    print(ew)

##    return(' '.join(j))
string='إِنَّا أَنْزَلْنَا عَلَيْكَ الْكِتَابَ لِلنَّاسِ بِالْحَقِّ فَمَنِ اهْتَدَى فَلِنَفْسِهِ وَ مَنْ ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا وَ مَا أَنْتَ عَلَيْهِمْ بِوَكِيلٍ'
string='إِنَّا أَنْزَلْنَا عَلَيْكَ الْكِتَابَ لِلنَّاسِ بِالْحَقِّ فَمَنِ اهْتَدَى فَلِنَفْسِهِ وَ مَنْ ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا وَ مَا أَنْتَ عَلَيْهِمْ بِوَكِيلٍ (زمر / آیه ۴۱)إِنَّا أَنْزَلْنَا عَلَيْكَ الْكِتَابَ لِلنَّاسِ بِالْحَقِّ فَمَنِ اهْتَدَى فَلِنَفْسِهِ وَ مَنْ ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا وَ مَا أَنْتَ عَلَيْهِمْ بِوَكِيلٍ (زمر / آیه ۴۱)'

##string='هتجداتاگ'
string=string.replace(' ','1').replace('(','1').replace(')','1').replace('/','1')
#searchifinarray1(string)
w='11441111443224441125243314112414461121242444111521112413163534441112464133352444351512223444182435114434113318242524331211223411114446252433123421221433'
b='4411442342441152421142641112424244115112114231615343441121641453424453512122434442534443114252422111224311446452422143122242'
ser=' 1/1 و 4/4 و 1/1 و 1/1 و 1/1 و 4/4 و 3/2 و 2/4 و 4/4 و 1/1 و 1/1 و 2/5 و 2/4 و 3/3 و 1/4 و 1/1 و 1/1 و 2/4 و 1/4 و 4/6 و 1/1 و 2/1 و 1/1 و 2/4 و 2/4 و 4/4 و 1/1 و 1/5 و 1/1 و 2/1 و 1/1 و 2/4 و 1/3 و 1/6 و 1/1 و 3/5 و 3/4 و 4/4 و 1/1 و 1/1 و 1/2 و 4/6 و 4/1 و 3/3 و 1/1 و 3/5 و 2/4 و 4/4 و 3/5 و 1/5 و 1/2 و 1/1 و 2/2 و 1/1 و 3/4 و 4/4 و 1/1 و 1/8 و 2/4 و 1/1 و 3/5 و 1/1 و 4/4 و 3/4 و 1/1 و 1/1 و 3/3 و 1/8 و 2/4 و 1/1 و 2/5 و 2/4 و 3/3 و 1/2 و 1/1 و 1/1 و 2/2 و 1/1 و 3/4 و 1/1 و 1/1 و 1/1 و 4/4 و 4/6 و 1/1 و 2/5 و 2/4 و 3/3 و 1/2 و 3/4 و 1/1 و 2/1 و 2/2 و 1/4 و 3/3 و 2/4 و 1/1 و 1/1 و 3/2 و 3/4 و 2/6 و 1/1 و 1/1 و 1/1 و 1/1 و 3/3 و 1/2 و 1/1 و 1/1'
keye=re.sub(r'[^0-9]','',ser)
print(keye)

ese='1144111111443224441111252433141111241446112111242444111511211124131611353444111112464133113524443515121122113444111824113511443411113318241125243312111122113411111144461125243312341121221433241111323426111111113312114411'
def coer(string):
    ew=''
    k=0
    for i in string:
        if k%2==0:
            ew+=i
        k+=1
    print(ew)
bases='14111432411223111214121224111212111334111443132431112134112131431131212231112131114412231312213211332111131141'[::-1]
#base12(w[::-1])

##    print(a)
##baseconverter('12a22+214310//10111+')
reader=b'011010011100110110011110010100011101011011110110'
##print((int('4',16))**3)           
#print(decode_to_str(reader, codecs.ITA2_US))
##baseconverterstep0
'''
string='70 6 65 61 73 65 20 64 6 6 27 74 20 74 65 78 74 20 6 65 0a 6 6b 3 0a 0a 69 20 74 6 6 64 20 75 20 74 68 61 74 20 62 65 66 6 72 0a 0a 69 20 64 6 6 27 74 20 77 61 6 74 20 74 61 6 6b 20 74 6 20 75 0a 0a 49 20 64 6 6 27 74 20 77 61 6 74 20 74 6 20 62 65 20 69 6 20 63 6 6 74 61 63 74 20 77 69 74 68 20 79 6 75 0a 0a 6 6 20 74 65 78 74 20 6 6 20 70 68 6 6 65 63 61 6 6 20 6 6 74 68 69 6 67 0a 0a 6 6b 3'
string=string.split(' ')
xd=[]
for i in string:
    i=i[::-1]
    b=0
    b=(int(i[0],16))
    if len(i)>1:
        b+=(int(i[1],16))*12
    xd+=[b]
print(xd)
'''
ser='''20 6 13 6 4 1 18 6 6 3 6 6 21 14 6 6 1 14 3 6 6 3 18 3 14 18 3 6 6 3 6 17 3 1 18 4 3 18 21 18 6 6 3 6 4 3 14 21 3 6 18 3 18 6 21 3 18 2 6 6 11 3 2 3 3 6 18 3 20 6 21 18 3 18 6 21 3 18 2 6 6 11 3 4 6 14 21 3 18 21 1 18 3 3 3 11 6 6 18 3 4 20 6 14 6 3 18 3 14 18 3 18 2 6 6 11 3 14 6 21 14 6 14'''
ser.replace(' ','')

print('###############')
string='غم زار تاریخ داد خیرات راز مغ'
print(searchifinarray1(string))
#331241232414232142133
#33312412324142321421333
string='غم زار تاریخ داد خیرات راز مغ'.replace(' ','')

print(len(string))
print(len('331241232414232142133'))
def numconverter(string):
    key='0123456789'
    key1=['','I','II','III','IV','V','IX','L','VIII','IXX']
    key2=['O','I','Z','E','H','S','G','L','B','G']
    key3=['','I','II','III','VI','V','IX','L','VIII','VI']
    key4=['','I','II','III','VI','V','IX','L','IVI','VI']
    listno=[key1,key2,key3,key4]
    for i in listno:
        zil=''
        for b in string:
            zil+=i[key.index(b)]
        print(zil)
numconverter('33312412324142321421333')
listnum=[
'33312412324142321421333',
'73105505260006250550137',
'84216616371117361661248' 
    ]

sere=[
'IIIIIIIIIIIIIVIIIIIIIIIVIIVIIIIIIIIIVIIIIIIIIIIII',
'EEEIZHIZEZHIHZEZIHZIEEE',
'IIIIIIIIIIIIVIIIIIIIIIVIIVIIIIIIIIIVIIIIIIIIIIIII',
'IIIIIIIIIIIIVIIIIIIIIIVIIVIIIIIIIIIVIIIIIIIIIIIII',
'IIIIIIIIIIIIIVIIIIIIIIIVIIVIIIIIIIIIVIIIIIIIIIIII',
'EEEIZHIZEZHIHZEZIHZIEEE',
'IIIIIIIIIIIIVIIIIIIIIIVIIVIIIIIIIIIVIIIIIIIIIIIII',
'IIIIIIIIIIIIVIIIIIIIIIVIIVIIIIIIIIIVIIIIIIIIIIIII',
'LIIIIVVVIIIXIXIIVVVIIIIL',
'LEIOSSOSZGOOOGZSOSSOIEL',
'LIIIIVVVIIIXIXIIVVVIIIIL',
'LIIIIVVVIIIXIXIIVVVIIIIL',
'VIIIIVIIIIXIXIIXIIILIIILIIIIXIIXIXIIIIVVIII',
'BHZIGGIGELIIILEGIGGIZHB',
'VIIIVIIIIIXIXIIXIIILIIILIIIIXIIXIXIIIVIVIII',
'IVIVIIIIIXIXIIXIIILIIILIIIIXIIXIXIIIVIIVI',
]

def numconvert(string):
    key=['I','V','X','L']
    key1=[1,5,10,50]
    key2=['1','101','10','1010']
    try:
        zil=''
        for i in string: 
             zil+=key2[key.index(i)]
        print(zil)
    except:
        ew=2

for i in sere:
    numconvert(i)
satrr="ابجدهوزحطیکلمنسعفصقرشتثخذضظغ"
text='غمزارتاریخدادخیراترازمغ'
satrre='غمزارتاریخدادخیراترازمغابجدهوزحطیکلمنسعفصقرشتثخذضظغ'
text='غمزاریارتجدادجترایرازمغ'
sttringr=text+satrr
def cleanit(string):
    ze=''
    for i in string:
        if i not in ze:
            ze+=i
    return(ze)
print(cleanit(sttringr))
self='غمزارتیخدبجهوحطکلنسعفصقشثذضظ'
reve='غمزارتیخدظضذثشقصفعسنلکطحوهجب'
ast='صثقفغهخحجچشسیبلاتنمپطزردوکگ'

def checkit():
    LETTERS="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
    
    satrr="ابجدهوزحطیکلمنسعفصقرشتثخذضظغ"
    abtash=satrr[::-1]
    self='غمزارتیخدبجهوحطکلنسعفصقشثذضظ'
    reve='غمزارتیخدظضذثشقصفعسنلکطحوهجب'
    ast='صثقفغهخحجچشسیبلاتنمپطزردوکگX'
    ammr='غمزاریتجدظضذخثشقصفعسنلکطحوهب'
    amme='غمزاریتجدبهوحطکلنسعفصقشثخذضظ'
    alpahlist=[satrr,abtash,self,reve,ast,ammr,amme]
    
    for i in alpahlist:
        
        for z in alpahlist:
            zivar=''
            for b in z:
                we=i[z.index(b)%len(i)]
                me=[z.index(b)%len(i)]
                if we in i:
                    zivar+=z[i.index(we)%len(z)]
            print(zivar)
##checkit()
#    ^
#SyntaxError: unexpected EOF while parsing     
##checkit('')
def sezarnew(message,key):
 LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() 
 for key in range(len(LETTERS)):
     translated = ''
     for symbol in message:
         if symbol in LETTERS:
             num = LETTERS.find(symbol)
             num = num - key
             
             if num < 0:
                  num = num + len(LETTERS)
                  translated = translated + LETTERS[num]
                  
             else:
             
                  translated = translated + LETTERS[num]
     a=('Key #%s: %s' % (key, translated))
     b=str((translated))
     #c25.write(((b))+"\n")
     return(b)
def shifttext(string):
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    string=string.split(' ')
    z=''
    n=''
    for i in string:
        if i[0].isupper():
            z+=' '
            n+=' '
            i=i.lower()
            c=LETTERS.index(i[0])
            if c<13:
                c+=1
##            if c>13:
                
            for b in i:
             if b in LETTERS:   
                
                g=LETTERS.index(b)
                z+=LETTERS[((LETTERS.index(b))-c)%(len(LETTERS))]
                n+=LETTERS[((LETTERS.index(b))+c)%(len(LETTERS))]
        elif i[0].isupper()==False:
            z+=' '+i
            n+=' '+i
##                z+=str(LETTERS.index(b))+' '
    print(z)
    print(n)

shifttext('''Roses are White but often Rede
Yellow has a number and so does Bluee
Go back to the first puzzle piece without further adoe''')
shifttext('Cookie blow')
shifttext('''It might have shown you only one door, beware that the rabbits nest may contain a whole lot more.''')
awe='.--,....,.-,-;.-,.-.,.;...,.--.,---,-.,...,---,.-.,.,-..;--,.,...,...,.,--.,.,...,..--..'
class Solution(object):
   def rotate(self, matrix):
      temp_matrix = []
      
      column = len(matrix)-1
      for column in range(len(matrix)):
         temp = []
         for row in range(len(matrix)-1,-1,-1):
            temp.append(matrix[row][column])
         temp_matrix.append(temp)
      for i in range(len(matrix)):
         for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
      return matrix

##ob1 = Solution()
##print(ob1.rotate([[1,5,7],[9,6,3],[2,1,3]]))

def findpossible(string):
    ae=len(string)
##    ae=140
    z=2
    possible=[]
    while z<=(ae//2):
        if ae%z==0:
            possible+=[[str(z),str(ae//z)]]
        z+=1
    return(possible)
#
##print(findpossible(awe))
def textcutting(string,cutorder):
    min=[]
    for i in cutorder:
        m=int(i[0])
        print(m)
        max=[]
        z=0
        while z<len(string):
            
            max+=[string[z:z+m]]
            z=z+m
        
        min+=[max]
    return(min)
##print(textcutting(awe,findpossible(awe)))
##print(findpossible(awe))
ob1 = Solution()
def transpose(string):
    a=len(string)
    b=len(string[0])
    z=b-1
    m=[]
    while z>=0:
        for i in string:
            m+=[i[z]]
        z-=1
    az=(''.join(m))
    aze=az.replace('-','@').replace('.','-').replace('@','.')
    print(az)
    print(aze)
def getdthemout(string):
    for i in string:
        transpose(i)
##getdthemout(textcutting(awe[::-1],findpossible(awe)))
awe1='''بکِش ای عشقِ کلی جزوِ خود را
که این جا در کشاکش‌ها زبونم

ز هجرت می‌کشم بارِ جهانی
که گویی من جهانی را سُتونم'''
ewer='testit for rapind contetn'
print(getdthemout(textcutting(ewer,findpossible(ewer))))
##print(findpossible(ae2))
##zsdd=['.--,', '....', ',.-,', '-;.-', ',.-.', ',.;.', '..,.', '--.,', '---,', '-.,.', '..,-', '--,.', '-.,.', ',-..', ';--,', '.,..', '.,..', '.,.,', '--.,', '.,..', '.,..', '--..']    
##transpose(zsdd)
print('#######')
'''
with open ('berk2','r') as file1:
    for line in file1:
        base12(line)
        base12(line[::-1])
'''
string='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت عتا ت'
string1='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت ع تا ت'
string2='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت ع تا ت '
string3='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت ع تا ت هستیم.'
string4='سلام وقت بخیر۱ نیازمند یک فروشنده لوازم ارایشی از ساعت ع تا ت هستیم.'
##string='غم زار تاریخ داد خیرات راز مغ'
listing=[string,string1,string2,string3,string4]
aerw='ابجدهوزحطیکلمنسعفصقرشتثخذضظغ'
##print(aerw[21])
##print(aerw[15])
a='.--.-.--....---.--.-......-.-...-...-..-..-..---.---.-.-...-...---..------.-...---......--..-----.----.--.-...--....--.--..-.....------....-.-...-.---.-.--..--...--...-.-.-.--.--.-..-...-.-.--...-.....'
##.--.-.--....---.--.-......-.-...-...-..-..-..---.---.-.-...-...---..------.-...---......--..-----.----.--.-...--....--.--..-.....------....-.-...-.---.-.--..--...--...-.-.-.--.--.-..-...-.-.--...-.....
b='--..----.-.-.........-..---.--.----....-.-.-.-...-.-...----.-.-...-...-...-.-.-.-.-......--..-..-..---...........--.---.---.-..--.-......--.---.---.-.---.-.-.--...-.-..---.-.---...----.---..---..-..-..'
def counterfortap(string):
    p=[]
    d=0
    c=1
    while d<(len(string)-1):
        if string[d]==string[d+1] and (d+1)!=(len(string)-1):
            c+=1
            d+=1
        elif string[d]!=string[d+1] and (d+1)!=(len(string)-1):
            
            p+=[c]
            c=1
            d+=1
        elif string[d]!=string[d+1] and (d+1)==(len(string)-1):
            
            p+=[c]
            c=1
            p+=[c]
            d+=1
        else:
            c+=1
            p+=[c]
            d+=1
    print(p)
counterfortap(b)
dsewe='''Gah. Your tab just crashed.
We can help!

Choose Restore This Tab to reload the page.
Will you help us?

Crash reports help us diagnose problems and make Firefox better.
Report this tab
Send an automated crash report so we can fix issues like this
Report background tabs
Update preferences to automatically submit reports when Firefox crashes'''
print(re.sub(r'[Store This Tab]','',dsewe))