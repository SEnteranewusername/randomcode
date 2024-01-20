def abjadorper(string):
    alphabet = ["ابجد","هوز","حطی","کلمن","سعفص","قرشت","ثخذ","ضظغ"]
    
    b=[]
    for i in string:
        n=0
        while n<len(alphabet):
            if i in alphabet[n]:
                z=0
                while z<len(alphabet[n]):
                    if i == alphabet[n][z]:
                        b+=[[(n),(z)]]
                    z+=1
            n+=1
    return(b)
def keymakerforbase32p(string):
    alphabet=''
    string=string+alphabet
    m=[]
    for i in string:
        if i not in m:
            m+=[i]
    z=0
    d=[]
    while z<len(m):
        d+=[m[z:z+8]]
        z+=8
    return(d)
def base32azjah(string,key):
    key=keymakerforbase32p(key)
    string=abjadorper(string)
    decoded=''
    for i in string:
        decoded+=key[i[1]][i[0]]
    return(decoded)
listofbase32=[
    '23456789CFGHJMPQRVWXcfghjmpqrvwx'
    ,'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
    ,'YBNDRFG8EJKMCPQXOT1UWISZA345H769'
    ,'0123456789ABCDEFGHIJKLMNOPQRSTUV'
    ,'0123456789BCDEFGHJKMNPQRSTUVWXYZ'
    ,"ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
    ]
a=['نفامنبا ر.دداکرشطع  ک‌رم رکررری‌لط م س  ما ر ج یوضعول ازومنو ن رظ'
,'ظر ن ونموزا لوعضوی ج ر ام  س م طل‌یرررکر مر‌ک  عطشرکادد.ر ابنمافن'
,'هر اد ررزمنلبمض   ر ودض یسواهزملاارادکهک‌کهپسهدمرینخاو.مااب م  '
  ,'م باام.واخنیرمدهسپهک‌کهکداراالمزهاوسی ضدو ر   ضمبلنمزرر دا ره'
  ,'ر تونا تره نیر ح   گهرضماستدوها ندایما همکهرخهعیح دیخدب هاتابت ن '
 ,'ن تباتاه بدخید حیعهخرهکمه امیادن اهودتسامضرهگ   ح رین هرت انوت ر'
   ,'ظاهرا در ستون سخن خوانندگانِ محترم امروز روزنامه کیهان، مطلبی در مورد عدم حضور حقیر در جنگ منتشر شده و در فضای مجازی دست به دست و مادرم هم از آن مطلع شده‌اند. پیامی برای برادرم ارسال کرده و امر کرده‌اند که در پاسخ به ادعای مطرح شده در کیهان پاسخی داده شود. برادرم هم برای اجابت امر با بنده تماس گرفتند. '
   ]

def bruteit(string,key):
    for i in string:
        for b in key:
           print(base32azjah(i,b))
           print(base32azjah(i[::-1],b))
           print(base32azjah(i,b[::-1]))
           print(base32azjah(i[::-1],b[::-1]))

def lenbased2key(string):
    string=string.split(' ')
    m=[]
    for i in string:
        m+=[len(i)]
    return(m)
def skipbasedkey(string,keym):
##    string=string.replace(' ','')
    string=[chr for chr in string]
    z,k=0,0
    m=''
    waht=''
    while (z)<len(string):
        m+=string[(int(keym[(k)%len(keym)])+z-1)%len(string)]
        waht+=string[(int(keym[(k)%len(keym)])+z-1)%len(string)]+'no='+str(z)+'no2='+str(k)

##        print((int(keym[(k)%len(keym)])+z))
        z,k=z+int(keym[(k)%len(keym)]),k+1
        
    #print(m)
##    print(''.join(string))
    #print(m[::-1])
    return(m)
a1='ظاهرا در ستون سخن خوانندگانِ محترم امروز روزنامه کیهان، مطلبی در مورد عدم حضور حقیر در جنگ منتشر شده و در فضای مجازی دست به دست و مادرم هم از آن مطلع شده‌اند. پیامی برای برادرم ارسال کرده و امر کرده‌اند که در پاسخ به ادعای مطرح شده در کیهان پاسخی داده شود. برادرم هم برای اجابت امر با بنده تماس گرفتند.'
b1='حسب الامر حاج‌خانوم، عین صوت ایشان برای اطلاع آن خواننده بزرگوار کیهان و همچنین گردانندگان این روزنامه، عینا پیوست و منتشر می کنم.'
#bruteit(a,listofbase32)
def brote(a1,b1):
    a2=a1.replace(' ','')
    b2=b1.replace(' ','')
    aw=[
    skipbasedkey(a2,lenbased2key(b1)),
    skipbasedkey(a2[::-1],lenbased2key(b1[::-1])),
    skipbasedkey(a1,lenbased2key(b1[::-1])),
    skipbasedkey(a1[::-1],lenbased2key(b1))]
    return(aw)
    
#brote(a1,b1) 
#print(abjadorper('مضر'))
bruteit(brote(a1,b1),listofbase32)