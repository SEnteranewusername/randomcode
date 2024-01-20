def mrmegha(line):
    a=9
    liststringchar=[char for char in line]
    while a**2<len(line):
        chare=[]
        b=0
        if len(line)%a**2==0:
           for i in liststringchar:
               ebo=""
               bl=len(line)//a**2
               if b%bl==0:
                   ebo=liststringchar[b]
                   chare=chare+[ebo]
               b=b+1
        print("".join(chare))
        #print(line)
        #print(a)
        a=a+1
def lenline(line):
    print(line)
    print(len(line)**.5)
def lenline2(line):
    if len(line)==400:
        print(line)
with open('maior34.txt', 'r') as file1:
 for line in file1:
  needle1 = line.strip()
  #lenline2(needle1)
  lenline2(needle1)
  