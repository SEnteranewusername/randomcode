LETTERS="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"

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
    return(decoded,decoded2)
def transporter():
    
    a='این لاله کیه که دیشب اومده خواب زیدم از صبح دهن منو سرویس کرد با لاله'
    c='سالوادور'
    v=0
    ae=[]
    while v<len(a):
        b=len(a)//len(c)
        cd=[chr for chr in ((a[v:(v+b)]).rjust(len(c),' '))]
        ae=ae+[cd]
        v=v+b
    print(ae)
transporter()