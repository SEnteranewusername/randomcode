import re
def replacemultipleinrow1(string):
    print(string.replace('0', ''))
    print(string.replace('0', '1'))
    print(string.replace('0', '3'))
    print(string.replace('0', '2'))
def keymaker(string):
    m=''
    for i in string:
        if i not in m:
            m+=i
    return(m)
def base3rotmpden(text):
    
    l1="*147g}~h^ipqrs?{}{?:_!`"
    l2=" 0258abcjkltuv"
    l3="#369defmnowxyz"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    waxee=[]
    for i in textew:
        if i in testp1:
            be="1"
            de='3'
        elif i in testp2:
            be="2"
            de='2'
        elif i in testp3:
            be="3"
            de='3'
        else:
            be=i
            de=i
        mexae=mexae+[be]
        waxee=waxee+[de]
##    print(mexae)    
    print("".join(mexae))
    print("".join(waxee))
def base3mpden(text):
    
    l1="abcdef12{}3)(*&^%$#`~"
    l2="ghfijklmno456"
    l3="pqrstuvwxyz789"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    waxee=[]
    for i in textew:
        if i in testp1:
            be="1"
            de='3'
        elif i in testp2:
            be="2"
            de='2'
        elif i in testp3:
            be="3"
            de='1'
        else:
            be=i
            de=i
        mexae=mexae+[be]
        waxee=waxee+[de]
##    print(mexae)    
    print("".join(mexae))
    print("".join(waxee))

def base3RPmpden(text):
    l1="gpajtdmw0123456789 "
    l2="hqbkuenx"
    l3="irclvfoy"
    l4='sz'
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    testp4=[chr for chr in l4]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        elif i in testp4:
            be="4"
        else:
            be=i
        mexae=mexae+[be]
##    print(mexae)    
    print("".join(mexae))
def englishmobile(string):
    base3rotmpden(string)
    base3mpden(string)
    base3RPmpden(string)
def basefa3mpden(text):
    l1="ايآئابپتث123.?!$#!٬:٫﷼٪×،*)("
    l2="جچحخدذرزژسشصض456"
    l3="ظطعقغکفگلمنیوهی789"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    waxee=[]
    for i in textew:
        if i in testp1:
            be="1"
            de='3'
        elif i in testp2:
            be="2"
            de='2'
        elif i in testp3:
            be="3"
            de='1'
        else:
            be=i
            de=i
        mexae=mexae+[be]
        waxee=waxee+[de]
   
    #print("".join(mexae))
    #print("".join(waxee))
    replacemultipleinrow(("".join(mexae)))
    replacemultipleinrow(("".join(waxee)))

def basefa3Rmpden(text):
    l1="369يئيآجچحخطظعغ"
    l2="852بپتثدذرزژفقکگلم0"
    l3="147سشصضنوهی*#!.$%?ا^:'؟!:"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    waxee=[]
    for i in textew:
        if i in testp1:
            be="1"
            de='3'
        elif i in testp2:
            be="2"
            de='2'
        elif i in testp3:
            be="3"
            de='1'
        else:
            be=i
            de=i
        mexae=mexae+[be]
        waxee=waxee+[de]
##    print(mexae)    
##    a=("".join(mexae))
    replacemultipleinrow(("".join(mexae)))
##    b=("".join(waxee))
    replacemultipleinrow(("".join(waxee)))
##    print(a)
##    print(b)
##    return(a,b)
def base10Men(string):
    a=['0 ','1?!,.','2abc','3def','4ghi','5jkl','6mno','7pqrs','8tuv','9wxyz']
    
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
    print(j)
    print(j[::-1])

def base10Menfa(string):
    a=['0 ','‌1‌‌?،!،,؟؟‌.','2بپتث','3ايآ','4سشصض','5دذرزژ','6جچحخ','7نوهی','8فقکگلم','9طظعغ']
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
                j=j+str(1)
    print(j)
    print(j[::-1])
print('somesidetest')
#strg=
strg=' وا،چرا یکی باید از حرف طرف مقابل خودشو بزنه ؟؟! اگه منطقی بود که جوابشو می‌دادی اگه مسخره بود که جواب نداشت'
base10Menfa(strg)
print('#############')
##alph=['صثقفغهخحجچ','شسیبلاتنمپ','#طزردوکگ','### ']
adminfum=['صثقفغهخحجچ','شسیبلاتنمپ','#طزردوکگ','!#: #.']
alph=['صثقفعهخحجچ','شسیبلاتنمپ','طزردوکگ','!#، #.']
def testmine(string):
    v=''
    for i in string:
        k=0
        
        while k<(len(alph)):
          if i in alph[k]:  
            c=((alph[k]).index(i)+1)
            v+=str(hex(c)[2:])+str(k+2)
            k=1000
          k=k+1
    return(v)
def poseinfasam(string):
    d=''
    c=''
    k=0
    for i in string:
        if k%2==1:
            d+=str(int(i)-1)
        if k%2==0:
            c+=str(int(i,16))
        k=k+1
    print(c)
    print(d)
    print(string)
    return(c)
def englishmobile(string):
    base3rotmpden(string)
    base3mpden(string)
    base3RPmpden(string)
    base10Men(string)

def famobile(string):
    basefa3Rmpden(string)
    basefa3mpden(string)
    poseinfasam(testmine(string))
    basefa3Rmpden((poseinfasam(testmine(string))))
    base10Menfa(string)
##    replacemultipleinrow((basefa3mpden(string))[0])
    
    
string4444='you really think that i am that stupid'
    

string8='سلام یک کارت دانشجویی ب نام ف.ن گم شده هرکی یافت اطلاع بده لطفا. '
string='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت اطلاع بده لطفا.سپاس'
string1='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت لطفا اطلاع بده. سپاس'
string2='سلام یک کارت دانشجویی ب اسم ف.ن گم شده هرکی یافت اطلاع بده لطفا.'
string3='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت لطفا اطلاع بده.سپاس'
string4='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت لطفا اطلاع بده. سپاس'
string5='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت اطلاع بده لطفا.سپاس'
string6='سلام یک کارت دانشجویی ب اسم ف.ن گم شده هرکی یافت اطلاع بده لطفا.1112859'
string7='سلام یک کارت دانشجویی ب اسم ف.ن گم شده هرکی یافت اطلاع بده لطفا. امین'


#,string1,string2,string3,string4,string5,string6,string7


##string='غم زار تاریخ داد خیرات راز مغ'
listing=[string,string1,string2,string3,string4,string5,string6,string7,string8]
def permulate(liste):
    for i in liste:
        b=string.replace(' ', 'ف').replace('.', 'ن')
        famobile(i)
        famobile(i[::-1])
        famobile(b)
        famobile(b[::-1])

##permulate(listing)
##print((testmine(string)))
##string='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت اطلاع بده لطفا.سپاس'

##poseinfasam(testmine(string))
##print(testmine(string))
##string='333353454343543332433535333525354353425244353323534335342534235'
##famobile(string)
##

##replacemultipleinrow('211211333 321 31331 1313 3323 32233 313 313 31 3322312 1213 33 3132')
##replacemultipleinrow('211211333 321 31331 1313 3323 32233 313 313 31 3322312 1213 33 3132')
def alphabetchecker(string,string2):
    x=string
    ce=[chr for chr in string2]
    z=0
    d=''
    for i in x:
        d+=ce[(i)%len(ce)]
        z+=i
    print(d)
string2='And I will feed them that oppress thee with their own flesh; and they shall be drunken with their own blood, as with sweet wine: and all flesh shall know that I the LORD am thy Saviour and thy Redeemer, the mighty One of Jacob. (Isaiah, 49:26)'
string=[84, 6, 77, 73, 87, 77, 24, 76, 6, 6, 31, 88, 24, 88, 77, 92, 88, 24, 6, 77, 10, 6, 83, 3, 10, 10, 81, 24, 88, 6, 6, 76, 24, 89, 24, 88, 80, 73, 88, 24, 74, 77, 78, 6, 86, 10, 10, 81, 24, 76, 6, 6, 31, 88, 24, 91, 73, 6, 88, 24, 88, 73, 6, 83, 24, 88, 6, 24, 89, 10, 10, 57, 24, 76, 6, 6, 31, 88, 24, 91, 73, 6, 88, 24, 88, 6, 24, 74, 77, 24, 81, 6, 24, 75, 6, 6, 88, 73, 75, 88, 24, 91, 81, 88, 80, 24, 93, 6, 89, 10, 10, 6, 6, 24, 88, 77, 92, 88, 24, 6, 6, 24, 84, 80, 6, 6, 77, 75, 73, 6, 6, 24, 6, 6, 88, 80, 81, 6, 79, 10, 10, 6, 83, 3][::-1]
alphabetchecker(string,string2)


'''
string=['t text me',
't want talk to u',
't want to be in contact with you']
'''
string='''please donjt text me
ok?
i told u that befor
i donjt want talk to u
I donjt want to be in contact with you
no text no phonecall nothing
ok?'''
string='''please don't text me ok? ii told u that befor ii don't want talk to u I don't want to be in contact with you ino text no phonecall nothing iok?'''
string='''please don't text me
ok?

i told u that befor

i don't want talk to u

I don't want to be in contact with you

no text no phonecall nothing

ok?'''

##
string5='94 90 85 81 97 85 28 84 93 92 33 98 28 98 85 a0 98 28 91 85 a 93 8b 53 a a 89 28 98 93 90 84 28 99 28 98 88 81 98 28 82 85 86 93 96 a a 89 28 84 93 92 33 98 28 9b 81 92 98 28 98 81 90 8b 28 98 93 28 99 a a 61 28 84 93 92 33 98 28 9b 81 92 98 28 98 93 28 82 85 28 89 92 28 83 93 92 98 81 83 98 28 9b 89 98 88 28 a1 93 99 a a 92 93 28 98 85 a0 98 28 92 93 28 94 88 93 92 85 83 81 90 90 28 92 93 98 88 89 92 87 a a 93 8b 53'
##englishmobile(' kw  dwuriwwtwwl ewwretwwtiteitww  twhtriu ti liww twuteltwitiwl tiswwbts  ttwitkwlitiwl tiswwbtu   w eltilritttbwwitu   kw ewtiteitiswwbtewlewe')
def replacemultipleinrow(string):
    print(string.replace(' ', ''))
    print(string.replace(' ', '1'))
    print(string.replace(' ', '3'))
    print(string.replace(' ', '2'))
dse=['223223321133233223331323321231233222312112221221332232232231213222113322122223122321213222113322222232322121122223312222223233212312113322332333',
'223223323333233223333323323233233222332332223223332232232233233222333322322223322323233222333322222232322323322223332222223233232332333322332333',
' 23  13332333332 1333133332312333  3323323 32 2233 3333123323232 32333133  3332323223232 32333133   3 1232232333133233   23 13323123233313132131',
' 21  31112111112 3111311112132111  1121121 12 2211 1111321121212 12111311  1112121221212 12111311   1 3212212111311211   21 31121321211131312313',
' 21  11233111113 2113211113123111  1121332 13 3311 1121231131313 13411214  1113121331313 13411212   1 2313333111211312   21 21131231341121213212',
'059003987499899503997389984834899008948748084054990898835894849508479928700889485954849508479928800090358457488829948800059039848348479928395393',
'393593829974843848930950008849928884754853090008829974805948459584988007829974805948498538898099450480847849800998438489983799305998994789300950']
for i in dse:
    replacemultipleinrow(i)
    replacemultipleinrow(i[::-1])
base3RPmpden(' kw  dwuriwwtwwl ewwretwwtiteitww  twhtriu ti liww twuteltwitiwl tiswwbts  ttwitkwlitiwl tiswwbtu   w eltilritttbwwitu   kw ewtiteitiswwbtewlewe')
string='''please don't text me
ok?

i told u that befor

i don't want talk to u

I don't want to be in contact with you

no text no phonecall nothing

ok?'''
a=[]
for char in string:
    if char not in a:
        a+=[char]
print(''.join(a))
stringo='edladsllnddaddellsddllsaddalnalslnaddadloallnsalnellnddadsalseladlnalndelalneddllaeaadlnaedellnalndelalneddllasdlselalnelllnaaallddlnasedlsdalnalslnalneddllalsdellsdls'
base3RPmpden(stringo)
print(len('21311433211111233411334111132134321111133133241322332111141342311321321231322113312111321212332132123132211331413423132233321113311321421341132134321322113313412334134'))

#and then we should have few way! extermly genius way! i mean its so good! its so funny.
#then i mean we have just few way/// and we did not code for them.
#so we can use the linux code as shown there but a man should stand with his word be fore using linux excpet the deal has dsfjshtserhiasehrsea
# or we can use base13 as it has checksum system on its own! wow.
# or we can use some other way which we did not code for that.
#and this is the proof you were looking for.i hope feel satisfy with the result.
def base10Men310(string):
    a=['0 ','1?!%/:&=,.·.-_','2abc','3def','4ghi','5jkl','6mno','7pqrs','8tuv','9wxyz']
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
    print(j)
    print(j[::-1])
##base10Men()
def stringchanger(string):
    z=''
    for i in string:
        if i.isupper():
            i='#'+i.lower()
        z+=i
    return(z)
string='''https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fchannel%3Dfs%26client%3Dubuntu%26q%3Dim%2Bnot%2Bangry&q=EgRTexV3GLHo4qkGIjBptdV73-uZy2F9uyI5QTi3hChg12BNnhiw1WP1bQ-WIcVYzP6MjQE4L1fFlOCcOsEyAXJaAUM#'''[::-1]
stringchanger(string)
base10Men310(stringchanger(string))
def changecap(string):
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    cap='CAPTCHA'
    wam='bz'
    for i in string:
        wer=2
base10Men('client=ubuntu')
#so many path way! thats so cool! i mean! only a human can be that stupid to get one of them and leave the other! fudcking s
#ha! thats extremly funny! logical order, base 3 key, fucking regedit, fucking 1,2,3 rotation base, fucking base root, fucking sq root, fucking fucking. ha. lol.
def part2(string):    
    m=''
    for i in string:
        
        if i not in m:
            m+=i
    return(m)
def spliterlogically(string):
    string=string.split('=')
    z=0
    f=''
    for i in string:
        g=part2(i)
        if z%2==0:
            f+=g+'='
        if z%2==1:
            f+=','+g+','
        z+=1
    print(z)
    
def countchar(string):
    k=0
    for i in string:
        
        if i=='=':
            k+=1
    print(k)
print(spliterlogically(string))
countchar(string)
string='''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; charset=utf-8"><meta name="viewport" content="initial-scale=1"><title>https://www.google.com/search?channel=fs&amp;client=ubuntu&amp;q=im+not+angry</title></head>
<body style="font-family: arial, sans-serif; background-color: #fff; color: #000; padding:20px; font-size:18px; overscroll-behavior:contain;" onload="e=document.getElementById('captcha');if(e){e.focus();} if(solveSimpleChallenge) {solveSimpleChallenge(,);}">
<div style="max-width:400px;">
<hr noshade size="1" style="color:#ccc; background-color:#ccc;"><br>
<div style="font-size:13px;">
Our systems have detected unusual traffic from your computer network.  Please try your request again later.  <a href="#" onclick="document.getElementById('infoDiv0').style.display='block';">Why did this happen?</a><br><br>
<div id="infoDiv0" style="display:none; background-color:#eee; padding:10px; margin:0 0 15px 0; line-height:1.4em;">
This page appears when Google automatically detects requests coming from your computer network which appear to be in violation of the <a href="//www.google.com/policies/terms/">Terms of Service</a>. The block will expire shortly after those requests stop.<br><br>This traffic may have been sent by malicious software, a browser plug-in, or a script that sends automated requests.  If you share your network connection, ask your administrator for help &mdash; a different computer using the same IP address may be responsible.  <a href="//support.google.com/websearch/answer/86640">Learn more</a><br><br>Sometimes you may see this page if you are using advanced terms that robots are known to use, or sending requests very quickly.
</div><br>

IP address: 37.129.252.33<br>Time: 2023-10-25T08:08:07Z<br>URL: https://www.google.com/search?channel=fs&amp;client=ubuntu&amp;q=im+not+angry<br>
</div>
</div>
</body>
</html>
'''
def unicodetest(string):
    for i in string:
        if ord(i)>256:
            print(i,ord(i))
unicodetest(string)
#its fake as hell to use reg with fish language! just in case.
def chartofuckingcol():
    with open ('fileq','r') as file1:
        de=[]
        for line in file1:
            de=de+[line]
        return(line)
def fuckingillugicalfuckingstupidfuckingbulsshittest(string):
    a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    de=''
    for i in string:
       if i not in a:
           de+=' '
       elif i in a:
           de+=i
    return(de)
string='https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fchannel%3Dfs%26client%3Dubuntu%26q%3Dim%2Bnot%2Bangry&q=EgRTexV3GLHo4qkGIjBptdV73-uZy2F9uyI5QTi3hChg12BNnhiw1WP1bQ-WIcVYzP6MjQE4L1fFlOCcOsEyAXJaAUM'
aew=(fuckingillugicalfuckingstupidfuckingbulsshittest(string.lower()))        

string='TGCPSNETYICNETWWWFPSCSPSCECCPWECCGDPDGFWABFPSASSCECDCSSCECCCFFNEEPEPCCOFNCCOVASCTHSCABSCTHSCBGSCTHSCGXGSCTHSCGYPSCTHSCPOSCTHSCOPDSCTHSDPQSCTHSQXQSCTHSQYACCABGBEEFDCBBACACEBBFCDBDCEDFBFGADAACDAFBFCEAFDBACDFFBDBPFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFCFOFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCEAFABBFDECDPDCDDFFAFCACCBEFDFDCDBEDEPQDAAFAFDDEAFFEEADAFDACDAAEQBDFEFDACCDCEFFAAEFACEFEFCCDDTBEDQQECCPSASSCECDCSSCECCCFFNEEPEPECDSSCECDCSSCECCCFFNECPEEPECPEPWPSCECDSSCECDCSSCECCCFFNECPEEPECPEPCCOFNCCOVABCTSCAREBBCTSCBREGBCTSCGXREGBCTSCGYREPBCTSCPREOBCTSCOREPDBCTSDREPQBCTSQXREQBCTSQYREACCABGBEEFDCBBACACEBBFCDBDCEDFBFGADAACDAFBFCEAFDBACDFFBDBPFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFCFOFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCEAFABBFDECDPDBCADBCFEDAAFEEBEAFBDDAAPQBFDAEDABAFAEBCEABAABECECBQDBBEAEFBDBFFDBBBECEBEBAABGGPOCABPSC'.lower()
base10Men310(string)
print('feeeeeeeeeeeeeeeeeee')
##englishmobile(string4444)
aew=' این 25 میلیون رو میخوای چجوری پس بدی بهم '[::-1]
aew='ا5لریوپدم'
##base10Menfa(aew)
##base10Menfa('بدی بهم')

##aeew='087207520420757660737678075077787805207730'
##print(re.sub(r'[87250]','$',aeew))


string='''Let me put my cards on the table. I think that Python is a terrible language and is a poor place to start your coding. Why? Because it differs in so many ways from a properly structured language. For me, I just can’t remember how to do a loop in Python, and I have to Google it every time. And, the usage of tabs (and spaces) to structure code and having no semi-colon just leaves me cold. I don’t like the way it creates classes and in how it can easily break. And the “pip install” command is not the most reliable in integrating libraries.'''
aere=' پلیز فشار دهید دکمه سیک را'
famobile(aere)
waew='*debug-mode*.'
##print(base10Men310(waew))
print('$$$$$$$$$$$$$$$$$$$$$$$$')
justest=' بالاخره ی جور ماکارونیههه دیگه'[::-1]
base10Menfa(justest)
justest='حالا پاستا یا اسپاگتی بودن چ فرقی داره'[::-1]
base10Menfa(justest)
defe=['همسر گریلیش'
'موراتا و بانو'
'دوست دختر آنتونوچی','همسر سابق دنی آلوز']
for i in defe:
    print(base10Menfa(i))
    print(base10Menfa(i[::-1]))
string8='سلام یک کارت دانشجویی ب نام ف.ن گم شده هرکی یافت اطلاع بده لطفا. '
string='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت اطلاع بده لطفا.سپاس'
string1='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت لطفا اطلاع بده. سپاس'
string2='سلام یک کارت دانشجویی ب اسم ف.ن گم شده هرکی یافت اطلاع بده لطفا.'
string3='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت لطفا اطلاع بده.سپاس'
string4='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت لطفا اطلاع بده. سپاس'
string5='سلام یک کارت دانشجویی به نام ف.ن گم شده هرکی یافت اطلاع بده لطفا.سپاس'
string6='سلام یک کارت دانشجویی ب اسم ف.ن گم شده هرکی یافت اطلاع بده لطفا.1112859'
string7='سلام یک کارت دانشجویی ب اسم ف.ن گم شده هرکی یافت اطلاع بده لطفا. امین'


#,string1,string2,string3,string4,string5,string6,string7

string='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت 16تا 22'
string1='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت 16 تا 22'
string2='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت 16 تا 22 '
string3='سلام وقت بخیر نیازمند یک فروشنده لوازم ارایشی از ساعت 16 تا 22 هستیم.'
string4='سلام وقت بخیر۱ نیازمند یک فروشنده لوازم ارایشی از ساعت 16 تا 22 هستیم.'
##string='غم زار تاریخ داد خیرات راز مغ'
listing=[string,string1,string2,string3,string4]

def permulate(liste):
    for i in liste:
        b=string.replace(' ', '').replace('.', '')
        famobile(i)
        famobile(i[::-1])
        famobile(b)
        famobile(b[::-1])
def numconverter(string,key):
    a='123456789'
    key=keymaker(keymaker(key)+a)
    z=[key[:3],key[3:6],key[6:]]
    b=''
    for i in string:
        k=0
        while k<3:
            if i in z[k]:
                b+=str(k+1)
                k=1000
            k+=1
    print(b)
print('#############################################')
##permulate(listing)
'''
with open('fatima','r') as file2:
    
    for line in file2:
        numconverter(line,'8293')
        numconverter(line[::-1],'8293')
        numconverter(line,'8293'[::-1])
        numconverter(line[::-1],'8293'[::-1])
'''
def justify(string):
    m=''
    for i in string:
        if i.isupper():
            m+='1'+i.lower()
        else:
            m+=i
    return(m)
string='''Roses are White but often Red.
Yellow has a number and so does Blue.
Go back to the first puzzle piece without further ado.'''

base10Men310(justify(string))
ZS='''176737 273 194483 288 63836 17331#1935569 427 2 686237 263 76 3637 125831#146 2225 86 843 34778 789953 74323 9484688 3878437 2361#'''
sz='''#1632 7348783 8864849 32347 359987 87743 348 68 5222 641#138521 7363 67 362 732686 2 724 9655391#13371 63836 882 384491 372 737671'''
##for i in ae:
    
def filer():
 with open('mni','r') as file1:
    for line in file1:
        numconverter(line,'')
sttr='It might have shown you only one door, beware that the rabbits nest may contain a whole lot more.'
ewewew='''به نام پیوند دهنده قلب ها
صرفا برای سرگرمی

کراشت پیدا کن
دلنوشته و توییت و موزیک پست کن
پیامت اینجا برامون بفرست:'''
rwwe='لینک کانال:'
##base10Menfa(rwwe)
stringbaeww='''https://googleads.g.doubleclick.net/aclk?sa=l&ai=CkwQl619bZeCnAaCF1PIPj727yA6Az72idKiwvMjTEdnZHhABIJfA2h9g7QKgAd_kreooyAEBqQJRsCPW5f6lPuACAKgDAcgDCqoEiQJP0Pr1CMg1Gvadx4DkuMWcLg_2re_ZDEtnsmYomlYTtkEfj1y_msL4tLjHBOhrZkB3GhFIPBKH8h8XNFYNI7ZrMcCCoNbiWNiFvPWsRvUlQujNWTuR7E0S8yEQJyww7MNqBu_V-LAMVRiwWH_SsILEqIUCA32ORGPFRSKNdlWZR08O8VbC8oAEMf8jCpTASacstyiPusm2bWt3-VivH907SDPMlgk0TTrY6xsLTKmjIOn8tOrpYkp6jMaZ6z-xXtcBPnFfWvN21bS0-ZqiGT2zJqmOVum0jll3vccpPnmx4I1E_BTrANjdg-xlZcoZNhLuBbJoB4qJWc-ZOLvioOc-A-Y94tFrf2KDwAS-yfiTugTgBAGIBYWBnO5MgAffnP7JA6gH2baxAqgHjs4bqAeT2BuoB-6WsQKoB_6esQKoB9XJG6gHpr4bqAeaBqgH89EbqAeW2BuoB6qbsQKoB4OtsQKoB_-esQKoB9-fsQLYBwHSCBQIgGEQARgdMgKKAjoCgEBIvf3BOvIIG2FkeC1zdWJzeW4tNTE4ODcxMjQzMTQ4MDM5NLEJ4hUxgJxB6ceACgOKCosDaHR0cHM6Ly9lbmdhZ2VtZW50cy5hcHBzZmx5ZXIuY29tL3YxLjAvYzJzL2NsaWNrL2FwcC9uYXRpdmVwYy8wODI4NDMwLTk0MzQwOT9hZl9tZWRpYV9zb3VyY2U9Z29vZ2xlJmFmX2NhbXBhaWduX2lkPTIwNjMyMjQwMjYxJmFmX2NhbXBhaWduX25hbWU9R1VfR29vZ2xlX0Rlc2t0b3BfRXZlcmdyZWVuX1JPV18yMzEwJmFmX2NhbXBhaWduPUdVX0dvb2dsZV9EZXNrdG9wX0V2ZXJncmVlbl9ST1dfMjMxMCZhZl9yPWh0dHBzJTNBJTJGJTJGZ29kc3VuY2hhaW5lZC5jb20lMkYlM0Z1dG1fc291cmNlJTNEZ29vZ2xlJTI2dXRtX21lZGl1bSUzRG1lZGl1bV8xJTI2dXRtX2NhbXBhaWduJTNER1VfR29vZ2xlX0Rlc2t0b3BfRXZlcmdyZWVuX1JPV18yMzEwJTI2dXRtX2NvbnRlbnQlM0Rjb250ZW50XzGYCwHICwHgCwGiDBAqDgoM5LSxAu61sQK1uLECqg0CSVLIDQHiDRMIw63eotjSggMVoAJVCB2P3g7p2BMNiBQE0BUBmBYB-BYBgBcB&ae=1&gclid=EAIaIQobChMIoMnfotjSggMVoAJVCB2P3g7pEAEYASAAEgKEGvD_BwE&num=1&cid=CAQSiwEAyAmmjVEfhVKQnH0pbOgniWBzVuNfmD3QLXkmYDgHS8iCPtp4zN0KvddhbKQliEjFn3Y9oxefv_3EWv69wf__uKY5YF1NHbYHtiMLd4gPa6G83HnB7Z1-IVTTwxbHqVRcAi0jiJdA-b8JD9rhdzLMjsIvRd09ZIDwBt7H4sLL66a7bncWS2Mqts_HGAE&sig=AOD64_3HGrbQN2FBB0jY_VPpGDV0hE4OGA&client=ca-pub-1274416353693598&rf=4&nb=7&adurl=https://godsunchained.com/%3Futm_source%3Dgoogle%26utm_medium%3Dmedium_1%26utm_campaign%3Dgu_google_desktop_evergreen_row_2310%26utm_content%3Dcontent_1%26gclid%3DEAIaIQobChMIoMnfotjSggMVoAJVCB2P3g7pEAEYASAAEgKEGvD_BwE'''.lower()
base10Men310(stringbaeww)
ewewe='''Download Gods Unchained Now.
Engage in strategic battles with divine
entities and mythical powers.
'''
base10Men310('Gods Unchained'.lower())
numconverter('488771114664532371413682532542516381225517215124125975619293262223174757279262972435498658336944224532249477542315736692327757727953657822254322432763475707712641482394358692541273193386769665988533519167548554264795234434725484896396479762226624964387977885785698877307893759997667281815268749941774537482232674737756359970868822862363852782722789478762298318484907737654508879697585654668867795765629691998227633986212701974482957668860555382277669441312872653419592696458225624759219658466212199483732539271934884842244299266564233677526442229274457427238228621697756216377562995464477427232274489327239228626727756246877562113775629137759294722744437274364552562432483326844423532193959394868346329657968746365653544894592623224652673247024665995263492889950295424299695994892985399552899595267296752392298997736899989634463695850697968949598997798992389928992989295563692642924293892557849656965796599563692642924293892542989718372989295907522802323799526399988915781896939563692642924293878389038223798939967349990829956268525978133656962949599794034295862585458549295238892442955925522056595609134132291266558639298929558423978921594512789741594512889584239789264292429385863718372989295907522802323799526399988915781896939584239789268267526756075225099509949294429442944322734665579286177518532740278543744376496336857446862582227347722664273028262921292422212311142543132424762246466636857446862582227347732392722345348312931686111243122774932926658334857640726464929886363375956934478427874960583342575435363996933813398699311859593164294846534472648346279114888992478722405453212853974395657487309943928744755662726297267871442317441263641344727623220591877438043464212543681221782112744163536935981731416217123875148877111463786242463312661133886176872313346645312688616334861336334861112688612267244613348146645313375867138374733617691231012688612668368133266836811126425431333242476224646663685744686258222734773239272234534831293'[::-1],'')

string='میبینمتخودشمیادپنجشنبه'
print('##########################3333')
with open('wine','r') as file:
    for line in file:
        line=line.strip()[::-1]
        #a=re.sub('r[^a-zN\.\ ]','',line)
        #base10Men310(line.lower())
        #base10Men310(a)
        print(line.replace('N','16'))
        print(line.replace('N','6'))
        
        