asas={'00':'0', '01':'1', '02':'2', '03':'3', '04':'4', '05':'5', '10':'6', '11':'7', '12':'8', '13':'9', '14':'A', '15':'B', '20':'C', '21':'D', '22':'E', '23':'F', '24':'G', '25':'H', '30':'I', '31':'J', '32':'K', '33':'L', '34':'M', '35':'N', '40':'O', '41':'P', '42':'Q', '43':'R', '44':'S', '45':'T', '50':'U', '51':'V', '52':'W', '53':'X', '54':'Y', '55':'Z'}
ew=asas.keys()
key_list = list(asas.keys())
val_list = list(asas.values())
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
alphnumerebase36(test)
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
    l3="سشصيضنوهيي"
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
def makeitready2(i):
        #i=sa
    #for i in bew:
        while (len(str(i))>20):
            print((int(i)%nnn))
            i=str(i)[:-1]

with open('tttt.txt', 'r') as file1:
    for line in file1:
        #needle1 = alphnumerebase36(line.strip())
        #melinda(needle1)
        #((dddon(str(int(line,16)))))
        #makeitready2(line)
       try: 
        needle=line.strip()
        #basefa3Rmpden(needle)
        #basefa3mpden(needle)
        #base3(needle)
        #print(needle)
       except:
            sd=2
        
base3Rmpden("gsmg.io 5 btc puzzle challenge")
base3mpden("gsmg.io 5 btc puzzle challenge")
base3en("gsmg.io 5 btc puzzle challenge")
#base3("رفتم پیش دکتر کوهستانی")
#base3en("and how much in taxes do you pay")
bbb.close()