import re
import urllib.parse
par="یهونملگکقفغعظطضصشسژزرذدخحچجثتپبا"
#LETTERS="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
LETTERS="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
#pal=[char for char in pa]
def sezarnew(message):
 LETTERS="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"   
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
     print(b)
def numsez(message):
    i=0

    while i<33:
        beew=[]
        neew=[]
        for b in message:
            if b>=i:
                c=b-i
            else:
                c=i-b
            beew=beew+[c]
        print(a1z26pdec(reversed(beew)))
        print(a1z26pdec(beew))
        #print((beew))
        #(((beew)))
        i=i+1
def abtashfa(message):
    par="یهونملگکقفغعظطضصشسژزرذدخحچجثتپبا"
    lipar=[char for char in par]

    for key in range(len(LETTERS)):
     translated = ''
     for symbol in message:
         if symbol in LETTERS:
             num = LETTERS.find(symbol)
             tr=lipar[num]
             translated=translated+tr
    print(translated)
def a1z26pdec(message):
    decoded=""
    decoded2=""
    #message=message.split(",")
    let=[char for char in LETTERS]
    
    for i in message:
        be=let[int(i)%len(let)]
        
        de=let[(int(i)-1)%len(let)]
        decoded=decoded+be
        decoded2=decoded2+de
    print(decoded)
    print(decoded2)
def a1z26penc(message):
    for key in range(len(LETTERS)):
     translated = []
     translated2 = []
     for symbol in message:
         if symbol in LETTERS:
             num = LETTERS.find(symbol)
             translated=translated+[num]
             translated2=translated2+[(num+1)]
    print(translated)
    print(translated2)
def convert_en_characters(input_str):
    """
        Assumes that characters written with standard persian keyboard
        not windows arabic layout
    :param input_str: String contains English chars
    :return: New string with related characters on Persian standard keyboard
    """
    mapping = {
        'q': 'ض',
        'w': 'ص',
        'e': 'ث',
        'r': 'ق',
        't': 'ف',
        'y': 'غ',
        'u': 'ع',
        'i': 'ه',
        'o': 'خ',
        'p': 'ح',
        '[': 'ج',
        ']': 'چ',
        'a': 'ش',
        's': 'س',
        'd': 'ی',
        'f': 'ب',
        'g': 'ل',
        'h': 'ا',
        'j': 'ت',
        'k': 'ن',
        'l': 'م',
        ';': 'ک',
        "'": 'گ',
        'z': 'ظ',
        'x': 'ط',
        'c': 'ز',
        'v': 'ر',
        'b': 'ذ',
        'n': 'د',
        'm': 'پ',
        ',': 'و',
        '?': '؟',
    }
    return _multiple_replace(mapping, input_str)
def _multiple_replace(mapping, text):
    """
    Internal function for replace all mapping keys for a input string
    :param mapping: replacing mapping keys
    :param text: user input string
    :return: New string with converted mapping keys to values
    """
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

asas={'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5','00':'0', '01':'1', '02':'2', '03':'3', '04':'4', '05':'5', '10':'6', '11':'7', '12':'8', '13':'9', '14':'A', '15':'B', '20':'C', '21':'D', '22':'E', '23':'F', '24':'G', '25':'H', '30':'I', '31':'J', '32':'K', '33':'L', '34':'M', '35':'N', '40':'O', '41':'P', '42':'Q', '43':'R', '44':'S', '45':'T', '50':'U', '51':'V', '52':'W', '53':'X', '54':'Y', '55':'Z'}
ew=asas.keys()
key_list = list(asas.keys())
val_list = list(asas.values())
nnn=115792089237316195423570985008687907852837564279074904382605163141518161494337

test="45425510"
base58al="123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
base58lis=[chr for chr in base58al]
def alphnumerebase36(test):
    e=0
    rete=""
    while e<len(test):
        position = key_list.index(str(test[e:e+2]))
    
        rete=rete+str(val_list[position])
        e=e+2
    print(rete)
def turntonumbase58(test):
    e=0
    rete=""
    while e<len(test):
        position = base58lis.index(str(test[e:e+1]))
        rete=rete+str(position)
        e=e+1
    print(rete)
    
#test="5045414314515432542134530035031131404541431451543254213453003503113150"[::-1]
test="222224212321410123233311112131222222"[::-1]
"""
30 24 08 14 11 29 53 14 09 08 20 22
14422021424324414452155
312241541301011534
1433340
3435442
35343430
14225210
"""
#alphnumerebase36(test)
def melinda(test):
    mex0="0000100011110001110000010110110101000111111101110011011111000101100000111100000111111001111110"[::-1]
    mex1='0000100011110001110000010110110101000111111101110011011111000101100000111100000111111001111110'
    mex2='0000100011110001110000010110110101000111111001110011011111000101100000111100000011111001111010'
    mex3='0000100011110001110000010110110101000111111011100110111110001011000001111000001111100111110'
    
    testp=[chr for chr in test]
    mexe=[]
    we=0
    mex=mex0[3:]
    for i in testp:
        z=mex[we]
        if int(z)==1:
            mexe=mexe+[i]
        we=((we+1)%len(mex))%(len(testp)-1)
        
    textwe="".join(mexe)
    print(textwe)

def cardip(text):
    mex=[3,2,5,3,3,4,4,2][::-1]
    testp=[chr for chr in text]
    mexe=[]
    we=0
    be=0
    z=0
    while z<(len(testp)-1):
        
        mexe=mexe+[testp[z]]
        z=z+mex[we%len(mex)]-1
        we=we+1
    textwe="".join(mexe)
    print(textwe)
def base3(text):
    l1="ضصثقفغعهخحجچپ"
    l2="شسيبلاتنمکگي"
    l3="یژيظطزرذدئو"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))
def base3en(text):
    l1="qwertyuiop[]QWERTYUIOP"
    l2="ASDFGHJKL;'asdfghjkl"
    l3="zxcvbnm,./?ZXCVBNM"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))
def base3mpden(text):
    l1="abcdefABCDEF"
    l2="ghfjklmnoGFHJKLMNO"
    l3="pqrstuvwxyzPQRSTUVWXYZ"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))
def base3Rmpden(text):
    l1="GHIPQRSghipqrs"
    l2="ABCJKLTUVabcjkltuv"
    l3="DEFMNOWXYZdefmnowxyz"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))
def basefa3mpden(text):
    l1="اآابپتث"
    l2="جچحخدذرزژسشصض"
    l3="ظيطعقکگلمنيوهي"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))
def basefa3Rmpden(text):
    l1="اآجچحخطظعغ"
    l2="بپتثدذرزژفقکگلم"
    l3="سشصيضنوهیيي"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))
bbb = open('moplll60555.txt', 'w')
def dddon(nes):
    a=[chr for chr in nes]
    while len(a)<79:
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
        a=a+[g]
    print(a)
    #bbb.write(str("".join(a))+ '\n')
nnn = 115792089237316195423570985008687907852837564279074904382605163141518161494337
bew=[
    5001020221605120302903594054370551230541004313044113512350802360316033116516212180103203127460514,
900102022160502654053032924058038321006210370331350520037110437037711606270394304161038052803,
13109001020221605026540530329049361406351505352170611038033142051520043203111804703732310631363,
131090202218050260317033113051336133311001022204025172505483805512105410230551106370702290342033,
1560001020221605026540530329049361406351505352170611038033142051520043203111804703732310631363,
1560015513069035804020221160512031662105820042170441216150793904100327033117053003719041803771,
504001020221605026540530329049361406351505352170611038033142051520043203111804703732310631363,
504020221048030285170538605511905421043140441130513310055110538320902440396410515038175405852,
]
def makeitready():
    for i in bew:
        while (len(str(i))>30):
            print((int(i)%nnn))
            i=str(i)[:-1]
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
# Calling digitalRoot function
#print (digitalRoot(num))
seprator('558 447 558 5520000 47')
# This code is contributed by Gitanjali.
def makeitready2(i):
        #i=sa
    #for i in bew:
        while (len(str(i))>20):
            print((int(i)%nnn))
            i=str(i)[:-1]
def makeitready3():
    for i in bew:
        #i=sa
        ie=255
        while ie>41:
            mex=i%(2**ie-1)
            print(mex)
            #i=str(i)[:-1]
            ie=ie-1
#makeitready3()
def counttap(text):
    l1="ابچدسطفن"
    l2="پجذشظقه"
    l3="تحرصعکو"
    l4="خزضغگی"
    l5="ثژل"
    l6="م"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    testp4=[chr for chr in l4]
    testp5=[chr for chr in l5]
    testp6=[chr for chr in l6]
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
        elif i in testp5:
            be="5"
        elif i in testp6:
            be="6"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))
def countnumitself(text):
    l1="ا"
    l2="پبتث"
    l3="حچحخ"
    l4="دذرزژ"
    l5="سشصض"
    l6="ظطعغ"
    l7="فقکگلم"
    l8="نوهی"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    testp4=[chr for chr in l4]
    testp5=[chr for chr in l5]
    testp6=[chr for chr in l6]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="2"
        elif i in testp2:
            be="3"
        elif i in testp3:
            be="4"
        elif i in testp4:
            be="5"
        elif i in testp5:
            be="6"
        elif i in testp6:
            be="7"
        elif i in testp7:
            be="8"
        elif i in testp8:
            be="9"
        else:
            be=i
        mexae=mexae+[be]
    print(mexae)    
    print("".join(mexae))


"""
with open('nosin.txt', 'r') as file1:
    for line in file1:
        #needle1 = alphnumerebase36(line.strip())
        #melinda(needle1)
        #((dddon(str(int(line,16)))))
        #makeitready2(line)
       try: 
        needle=line.strip()
        #dddon(needle)
        #print((hex(int(seprator(needle))))[2:])
        #alphnumerebase36((seprator(needle))[::-1])
        #basefa3Rmpden(needle)
        #basefa3mpden(needle)
        #base3(needle)
        #print(needle)
       except:
            sd=2

makeitready3()        
#base3Rmpden("gsmg.io 5 btc puzzle challenge")
#base3mpden("gsmg.io 5 btc puzzle challenge")
#base3en("gsmg.io 5 btc puzzle challenge")
"""
basefa3Rmpden("قربونت برم. من توی ماشینم با دوستان در مسیر شمال. فکر کنم فردا زنگ بزنیم بهتره نه؟")
#base3("رفتم پیش دکتر کوهستانی")
#base3en("and how much in taxes do you pay")
"""
bbb.close()
textbase=""
basefa3Rmpden(text)
countnumitself(text)
counttap(text)basefa3mpden(text)
base3Rmpden(text)
base3mpden(text)
base3en(text)
base3(text)
convert_en_characters(input_str)
a1z26pdec(message)
abtashfa(message)
numsez(message)
sezarnew(message)
"""
def skipcipher2keyplusnext(test_str):
    liststringchar=[chr for chr in test_str]
    keyed=[0,9,0,2,7,4,0,0,4,1,7]
    decodedstring=[]
    pose=-1
    ew=-1
    pew=[]
    while pose<len(liststringchar):
                ew=ew+1
                pose=pose+keyed[(ew)%len(keyed)]
                pew=pew+[pose]
                b=(liststringchar[(((pose)%(len(liststringchar))))])
                decodedstring=decodedstring+[b]
    print(("".join(decodedstring)))
def skipcipher2key(test_str):
    liststringchar=[chr for chr in test_str]
    keyed=[0,9,0,2,7,4,0,0,4,1,7]
    decodedstring=[]
    pose=-1
    ew=-1
    pew=[]
    while pose<len(liststringchar):
                ew=ew+1
                pose=pose+keyed[(ew)%len(keyed)]-1
                pew=pew+[pose]
                b=(liststringchar[(((pose)%(len(liststringchar))))])
                decodedstring=decodedstring+[b]
    sing=liststringchar[0]            
    print((sing+"".join(decodedstring)))
    #print(pew)
def skipcipher(test_str):
    #liststringchar=test_str.split()
    liststringchar=[chr for chr in test_str]
    mex=1
    while mex<10:
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
def last_alphabet_word(ne):
    rrw1=""
    ne=ne.split(" ")
    for line in ne:
        mine=line[0:1]
       # rrw1 += str(mine) + " "
        line=line[-1:]
        rrw1 += str(line) + " "
    return (rrw1)
def first_alphabet_word(ne):
    rrw1=""
    ne=ne.split(" ")
    for line in ne:
        mine=line[0:1]
       # rrw1 += str(mine) + " "
        line=line[0:1]
        rrw1 += str(line) + " "
    return (rrw1)
def nthalphabetofword(ne):

    ne=ne.split(" ")
    mex=1
    men=-1
    while mex<7:
        rrw1=""
        rrw2=""
        for line in ne:
            if ((len(line))-1)>=mex:
                mine=line[mex]
       # rrw1 += str(mine) + " "
                linez=line[men]
            else:
                mine=""
                linez=""
            rrw1 += str(linez) + ""
            rrw2 += str(mine) + ""
        print((rrw2))
        print(rrw1)
        mex=mex+1
        men=men-1
        
        #print(rrw2)
textt="قربونت برم. من توی ماشینم با دوستان در مسیر شمال. فکر کنم فردا زنگ بزنیم بهتره نه؟"
skipcipher2key(textt)
skipcipher2keyplusnext(textt)
skipcipher(textt)
print(last_alphabet_word(textt))
print(nthalphabetofword(textt))
print(sezarnew(last_alphabet_word(textt)))
print(sezarnew(first_alphabet_word(textt)))