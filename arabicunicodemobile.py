import re
def stringtochr(string):
    string=[chr for chr in string]
    return (string)
def finddiffrence(string,string1):
    string=stringtochr(string)
    string1=stringtochr(string1)
    k=0
    while k<len(string):
        if string[k]!=string1[k]:
            print(string[k],string1[k])
        k=k+1
def unprintable(string):
    b='بجدهوزحطيكلمىنصإعفإأضقرستثخذـاَـأيــْـــٍٰـــّـظغشءــَـــُـــِ'
##    b=
    string=stringtochr(string)
    d=''
    c=''
    for i in string:
        if i not in b:
            d+=i
            c+= '#'+str(ord(i))
    print(d)
    print(c)
string='إِنَّا أَنْزَلْنَا عَلَيْكَ الْكِتَابَ لِلنَّاسِ بِالْحَقِّ فَمَنِ اهْتَدَى فَلِنَفْسِهِ وَ مَنْ ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا وَ مَا أَنْتَ عَلَيْهِمْ بِوَكِيلٍ'
string1='إِنَّا أَنْزَلْنا عَلَيْكَ الْكِتابَ لِلنَّاسِ بِالْحَقِّ فَمَنِ اهْتَدى فَلِنَفْسِهِ وَ مَنْ ضَلَّ فَإِنَّما يَضِلُّ عَلَيْها وَ ما أَنْتَ عَلَيْهِمْ بِوَكيلٍ'
string='إِنَّاأَنْزَلْنَاعَلَيْكَالْكِتَابَلِلنَّاسِبِالْحَقِّفَمَنِاهْتَدَىفَلِنَفْسِهِوَمَنْضَلَّفَإِنَّمَايَضِلُّعَلَيْهَاوَمَاأَنْتَعَلَيْهِمْبِوَكِيلٍ'
string1='إِنَّاأَنْزَلْناعَلَيْكَالْكِتابَلِلنَّاسِبِالْحَقِّفَمَنِاهْتَدىفَلِنَفْسِهِوَمَنْضَلَّفَإِنَّمايَضِلُّعَلَيْهاوَماأَنْتَعَلَيْهِمْبِوَكيلٍ'

string3='بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيمِ اللّٰهُمَّ صَلِّ عَلَىٰ مُحَمَّدٍ سَيِّدِ الْمُرْسَلِينَ، وَخَاتَمِ النَّبِيِّينَ، وَحُجَّةِ رَبِّ الْعَالَمِينَ، الْمُنْتَجَبِ فِى الْمِيثَاقِ، الْمُصْطَفىٰ فِى الظِّلالِ، الْمُطَهَّرِ مِنْ كُلِّ آفَةٍ، الْبَرِىءِ مِنْ كُلِّ عَيْبٍ، الْمُؤَمَّلِ لِلنَّجَاةِ، الْمُرْتَجَىٰ لِلشَّفاعَةِ، الْمُفَوَّضِ إِلَيْهِ دِينُ اللّٰهِ، اللّٰهُمَّ شَرِّفْ بُنْيَانَهُ، وَعَظِّمْ بُرْهَانَهُ، وَأَفْلِجْ حُجَّتَهُ، وَارْفَعْ دَرَجَتَهُ، وَأَضِئْ نُورَهُ، وَبَيِّضْ وَجْهَهُ، وَأَعْطِهِ الْفَضْلَ وَالْفَضِيلَةَ، وَالْمَنْزِلَةَ وَالْوَسِيلَةَ، وَالدَّرَجَةَ الرَّفِيعَةَ، وَابْعَثْهُ مَقَاماً مَحْمُوداً يَغْبِطُهُ بِهِ الْأَوَّلُونَ وَالْآخِرُونَ، وَصَلِّ عَلَىٰ أَمِيرِ الْمُؤْمِنِينَ، وَوَارِثِ الْمُرْسَلِينَ، وَقَائِدِ الْغُرِّ الْمُحَجَّلِينَ، وَسَيِّدِ الْوَصِيِّينَ، وَحُجَّةِ رَبِّ الْعَالَمِينَ، وَصَلِّ عَلَى الْحَسَنِ بْنِ عَلِيٍّ إِمَامِ الْمُؤْمِنِينَ، وَوَارِثِ الْمُرْسَلِينَ، وَحُجَّةِ رَبِّ الْعَالَمِينَ، وَصَلِّ عَلَى الْحُسَيْنِ بْنِ عَلِيٍّ إِمَامِ الْمُؤْمِنِينَ، ووَارِثِ الْمُرْسَلِينَ، وَحُجَّةِ رَبِّ الْعالَمِينَ؛ '

def wordextractor(string,key):
    string=string.split(' ')
    z=1
    pci=''
    while z<(len(string)-1):
        b=int(key[(z*2)%(len(key)-1)])
            
        try:
            string1=string[b]
            
            pci+=string1[int(key[(z*2-1)%(len(key)-1)])]
        except:
            sed=2
        z=z+1    
    print(pci)

keystr='1/1 و 4/4 و 1/1 و 1/1 و 4/4 و 3/2 و 2/4 و 4/4 و 1/1 و 2/5 و 2/4 و 3/3 و 1/4 و 1/1 و 2/4 و 1/4 و 4/6 و 1/1 و 2/1 و 2/4 و 2/4 و 4/4 و 1/1 و 1/5 و 2/1 و 1/1 و 2/4 و 1/3 و 1/6 و 3/5 و 3/4 و 4/4 و 1/1 و 1/2 و 4/6 و 4/1 و 3/3 و 3/5 و 2/4 و 4/4 و 3/5 و 1/5 و 1/2 و 2/2 و 3/4 و 4/4 و 1/8 و 2/4 و 3/5 و 1/1 و 4/4 و 3/4 و 1/1 و 3/3 و 1/8 و 2/4 و 2/5 و 2/4 و 3/3 و 1/2 و 1/1 و 2/2 و 3/4 و 1/1 و 1/1 و 4/4 و 4/6 و 2/5 و 2/4 و 3/3 و 1/2 و 3/4 و 2/1 و 2/2 و 1/4 و 3/3 و 2/4'[::-1]
string='پیامبر (صلی الله علیه و آله)- [در خطبه‌ی غدیر فرمود:] ای مردم! تعداد شما بیش از آن است که در یک جلسه بتوانید با من دست دهید و بیعت کنید و خدای عزّوجلّ فرمان داده است که نخست از شما اقرار زبانی بگیرم که در مورد امیرالمؤمنین علی (علیه السلام) و رهبر بودن او و امامانی که پس از او می‌آیند و از نسل من و اویند اقرار کنید و به شما گفتم و اعلام کردم که ذرّیّه‌ی من از صلب اویند. اکنون همگان بگویید: ما شنوا و فرمانبردار و پذیرا و خشنود به آن چیزی هستیم که از سوی پروردگارمان که پروردگار تو نیز هست در مورد علی (علیه السلام) و فرزندانش ابلاغ کردی و در این مورد با دل و جان و دست و زبان بیعت می‌کنیم و بر این بیعت زندگی می‌کنیم و می‌میریم و برانگیخته می‌شویم. آن را تغییر و تبدیل نمی‌کنیم و در آن شکّ و تردید روا نمی‌داریم و از این عهد بر نمی‌گردیم و پیمان نمی‌شکنیم و از خداوند و امیرالمؤمنین علی (علیه السلام) و فرزندانش حسن و حسین (علیها السلام) که امامند و از صلب علی (علیه السلام) و ذرّیّه‌ی تو می‌باشند، اطاعت می‌کنیم. و من منزلت و مقام حسن و حسین (علیها السلام) را در پیشگاه خدایم و خودم به شما اعلام کردم و رساندم و آن دو سرور جوانان بهشتند و آن دو پس از پدرشان امامند و پیش از آنکه علی (علیه السلام) پدر آن دو باشد، من پدر ایشانم. اکنون بگویید: از خدای فرمانبرداریم و در این مورد با تو و علی و حسن و حسین و دیگر امامان (علیهم السلام) که گفتی عهد و پیمان می‌بندیم و این پیمان که برای علی (علیه السلام) می‌گیری از دل و جان و دست و زبان رضایت می‌دهیم و اگر بتوانیم دست بیعت هم می‌دهیم (دست در دست او می‌گذاریم)، وگرنه با زبان اقرار می‌کنیم و هرگز به فکر تغییر آن نخواهیم بود و در دل خود خیال بازگشت از آن را نخواهیم داشت و ما این عهد را به فرزندان خود و فرزندان دور خود [یعنی نوه‌ها و نتیجه‌ها و خانواده‌ی خود می‌رسانیم] و خدا را دراین‌باره گواه می‌گیریم و خداوند بهترین گواه است و تو و همه‌ی کسانی را که باید از ایشان اطاعت کرد، چه آشکار باشند و چه نهان و فرشتگان و لشکرهای خدا را گواه می‌گیریم و خداوند از هر گواهی بزرگتر است. ای مردم! چه می‌گویید؟ خداوند داننده‌ی هر سخن و اندیشه نهانی همگان است. هرکس رهنمون شده است به سود خویش رهنمون شده و هر آن کس گمراه شود به زیان خود گمراه شده است و هرکس بیعت کند با خدا بیعت کرده است.'
string='غم زار تاریخ داد خیرات راز مغ'
keye=re.sub(r'[^0-9]','',keystr)

alli='lk ffmdr reer'
d=alli.split(' ')
def itsofunny(string,key):
    key=[chr for chr in key]
    stron=[chr for chr in string]
    string=string.split(' ')
    z=1
    a=0
    st=''
    pow=''
    mow=''
    while z<len(key)-1 and a<len(string):
        st0=string[int(int(key[int(z)])+a-1)%(len(string))]
        c=int(int(key[int(z-1)]))-1
        pow+=st0
        if (len(st0)-1)>=c:
            st+=st0[c]
            a=a+int(key[int(z)])
        z=z+2
    print(st)
##    print(pow[::-1])
    string=stron
    j,k,m,ew=1,0,0,0
    eee=''
    ppp=''
    ewew=''
    rere=''
    
    while j<len(key)-1 and k<len(string):
        st0=string[int(int(key[int(j)])+k-1)%(len(string))]
        stp=string[int(int(key[int(j-1)])+k-1)%(len(string))]
        stp3=string[int(int(key[int(m)])+ew-1)%(len(string))]
        eee+=st0
        ppp+=stp
        j=j+2
        k=k+int(key[int(j)])
        ew=ew+int(key[int(m)])
        m=m+1
        ewew+=stp3
    print(eee)
    print(ppp)
    print(ewew)
    print(rere)

##wordextractor(string,keye)
'''its so funny'''
keye='3624537451461537381458385465685384451548183126153321431371537515'
##string='abcd efg hijkl mnopqr stuvw xyz 1234'
itsofunny(string[::-1],keye)
##wordextractor(string,'12241513')
def smartsezarkeyed(string,key):
    alphabet='abcdefghijklmnopqrstuvwxyzæøå'
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    
##    string=re.sub(r'[^0-9a-zA-Z]','',keystr)
##    string=[chr for chr in string]
    key=[chr for chr in key]
    pattern=['m','po','p']
    k=0
    z=0
    text=''
    for i in string:
        k=k%len(pattern)
        d=alphabet.index(i)
        if pattern[k]=='m':
            c=alphabet[(d-1)%len(alphabet)]
            e=d-z
        elif pattern[k]=='po':
            c=alphabet[(d+1)%len(alphabet)]
            e=d+z
        elif pattern[k]=='p':
            c=''
            
##            c=alphabet[(d+1)%len(alphabet)]
            e=d*z
        k+=1    
        z=e
        text+=c
    print(text)
    print(z)
    

##string='0669455210272741073767837'
string='shiftmozillaspaceshiftcrashshiftspacereporter'
##string='mozillacrashreporter'
string='jbmvyynjudvkjwhgjlwj'
string='ozillarasheporter'
smartsezarkeyed(string[::-1],'3')
unprintable(string3)
    