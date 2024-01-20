import re
class skip:
    def __init__(self, string, num):
        self.string = string
        self.num = num
        
    def string_prepration(string,num):
        extractspace=re.sub(r'[ ]','',string)
        extractedstring=[chr for chr in extractspace]
        string=[chr for chr in string]
        bothl=[extractedstring,string]
        a=0
        c=[]
        for m in bothl:
          m1=m
          m2=m1[::-1]
          m3=[m1,m2]
          for i in m3:
            w=[]
            count=0
            while count<len(i):
                mi=i[(a%len(i))]
                a=a+num
                w=w+[mi]
                count=count+1
            c=c+[w]
        for k in c:
            print(''.join(k))
    def string_prepration_pop(string,num):
        extractspace=re.sub(r'[ ]','',string)
        extractedstring=[chr for chr in extractspace]
        string=[chr for chr in string]
        bothl=[extractedstring,string]
        a=0
        c=[]
        for m in bothl:
          m1=m
          m2=m1[::-1]
          m3=[m1,m2]
          for i in m3:
            w=[]
            
            while len(i)>0:
                mi=i.pop(a%len(i))
                a=a+num
                w=w+[mi]
                
            c=c+[w]
        for k in c:
            print(''.join(k))
            print((''.join(k))[::-1])
    def string_prepration(string,num):
        extractspace=re.sub(r'[ ]','',string)
        extractedstring=[chr for chr in extractspace]
        string=[chr for chr in string]
        bothl=[extractedstring,string]
        a=0
        c=[]
        for m in bothl:
          m1=m
          m2=m1[::-1]
          m3=[m1,m2]
          for i in m3:
            w=[]
            count=0
            while count<len(i):
                mi=i[(a%len(i))]
                a=a+num
                w=w+[mi]
                count=count+1
            c=c+[w]
        for k in c:
            print(''.join(k))
    def string_prepration_popword(string,num):
        string=(string.strip()).split(' ')
        bothl=[string,string[::-1]]
        a=0
        c=[]
        ceee=[]
        for i in bothl:
            w=[]
            
            while len(i)>0:
                mi=i.pop(a%len(i))
                a=a+num
                w=w+[mi[0]]
                
            c=c+[w]
            counter=0
            minor=[]
            
            while counter<len(i):
                cew=(i[counter])[0]
                minor=minor+[cew]
            ceee=ceee+[minor]   
                
        for k in c:
            print(''.join(k))
            print((''.join(k))[::-1])
        for ki in ceee:
            print((''.join(ki)))
            print((''.join(ki))[::-1])
b='''ولی امسال برای اولین بار یک حسینیه رفتم ک اشکام شر و شر میریخت
متحول شدم
ن با روضه خونی هاااا!!!
با سخنرانی...
این فرد محشره!
جزو معدود افرادیه ک دیدم چقدر حرفای جالبی میزنه!
منی ک از سخنرانی لذت نمیبردم، اونجا نمیخواستم حتی یک ثانیه شو از دست بدم!
حرف های تکراری نمیزد! حرفایی میزد که ب دل مینشست؛
به قول پدرم که همیشه میگه: پای صحبتای هر اخوند و آدمی نباید بشینی، کسی ک عملش با حرفاش یکی نباشه صحبتاش ب دلت نمیشینه
خلاصه میخواستم اینجایی رو که من باهاش آشنا شدم رو ب شماهم  معرفی کنم. شاید شماهم خوشتون اومد'''
be=[7,10,15,17,40,8,5,6,1450]
for i in be:
    skip.string_prepration_pop(b,i)
    skip.string_prepration(b,i)
    skip.string_prepration_popword(b,i)
##adgbehcf
##adgbehcfskip('abcdefgh',3)
##        adgbehcf
    

##    skip.string_prepration()