def fuckingstupidass2(string):
    a=['11','12','13','14', '21', '22', '23', '24', '31','32', '33', '34', '41','42', '43', '44']
    b='123a456b789ce0fd'
    c='e7410852f963dcba'
    d='147e2680369fabcd'
    e='df0ec987b654a321'
    le0n=0
    bb=''
    cc=''
    dd=''
    ee=''
    while le0n<(len(string)-3):
        g=int((string[le0n:(le0n+2)]),2)+1
        s=int((string[(le0n+2):(le0n+4)]),2)+1
        
        m=str(g)+str(s)
        
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
        
    print(bb)
    print(cc)
    print(dd)
    print(ee)
def fuckingstupidass(string):
    a=['11','12','13','14', '21', '22', '23', '24', '31','32', '33', '34', '41','42', '43', '44']
    b='123a456b789c*0#d'
    c='*7410852#963dcba'
    d='147*2680369#abcd'
    e='d#0*c987b654a321'
    le0n=0
    bb=''
    cc=''
    dd=''
    ee=''
    while le0n<(len(string)-3):
        g=int((string[le0n:(le0n+2)]),2)+1
        s=int((string[(le0n+2):(le0n+4)]),2)+1
        
        m=str(g)+str(s)
        
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
        
    print(bb)
    print(cc)
    print(dd)
    print(ee)
s=63572+1106
b=41530
d=120+3000+7200+86400+86400+86400-(12*3600)-1800-240
print(d/(s-b))
ae='01111001111000111100010011000100110011000111110011000100111001100100111010111110001111010010011000110011100010011001110011001111001110001000'
print(len(ae))
d=''
for i in ae:
    d=d+i+i
##d=''
a=127

while a>1:
    b=bin(a)[2:]
    z=-1
    c=''
    for i in d:
        z=z+1
        k=b[z%(len(b)-1)]
        f=((int(k)+int(i)))
        c=c+str(f%2)
##    print(c)
    fuckingstupidass(c)

    a=a-1
    
def addtostring(string):
    
    string=[chr for chr in str(string)]
    m=''
    for i in string:
        m+= str(int(i)+1)
    print(m)

ae=[
    11302320023321211023233013111110022002231022321100002212033101133223213031000011,
12312132233300322013313113002200313121120201223221222312133131121212331003301202231110,
11302320023321211023233013111110022002231022321100002212033101133223213031000011,
12312132233300320311031220222213201102103023212102101313210233332313112333321301131110
    ]
for i in ae:
    addtostring(i)
    addtostring((str(i))[::-1])
def fuckingstupidass3(string):
    a=['11','12','13','14', '21', '22', '23', '24', '31','32', '33', '34', '41','42', '43', '44']
    b='123a456b789c*0#d'
    c='*7410852#963dcba'
    d='147*2680369#abcd'
    e='d#0*c987b654a321'
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
    print(bb)
    print(cc)
    print(dd)
    print(ee)
def fuckingstupidass4(string):
    a=['11','12','13','14', '21', '22', '23', '24', '31','32', '33', '34', '41','42', '43', '44']
    b='123a456b789ce0fd'
    c='e7410852f963dcba'
    d='147e2680369fabcd'
    e='df0ec987b654a321'
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
    print(bb)
    print(cc)
    print(dd)
    print(ee)
fuckingstupidass4('12224221423444432242434444312342421231232343141231221342333313324122413411444334232432')
