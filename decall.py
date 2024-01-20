#from baseconvert import *
import re
class decimaltoall():
    def allinall(line):
        line=line.upper() 
        line=re.sub(r"[^A-Z]", "", line)
        line=re.sub(r"[^AEIOU]", "1", line)
        line=re.sub(r"[^1]", "0", line)
        return(line)
    def whyonlyvowel(line):
        line=line.upper() 
        line=re.sub(r"[^A-Z]", "", line)
        line=re.sub(r"[^AEIOUY]", "1", line)
        line=re.sub(r"[^1]", "0", line)
        return(line)
    def baconke(line):
        line = re.sub('0', 'A', line)
        line = re.sub('1', 'B', line)
        return(line)
    def reveseobin(line):
        line = re.sub('A', '1', line)
        line = re.sub('B', '0', line)
        return(line)
    def reveseobakon(line):
        line = re.sub('0', 'B', line)
        line = re.sub('1', 'A', line)
        return(line)
def word_len_to_base10(newo):
    rrw1=""
    a=0
    n2=0
    newo= (newo.split(" "))
    for line in newo:
     a=a+1
     n= (base((len(line)), 10, 10,string=True))
     n2=len(line)+n2
     rrw1 += str(n) + " "
    return (rrw1)
def word_len_to_base1033(newo):
    rrw1=""
    a=0
    n2=0
    newo= (newo.split(" "))
    for line in newo:
     a=a+1
     n= len(line)
     n2=len(line)+n2
     rrw1 += str(n) + " "
    return (rrw1)
def word_counrt_to_base10(newo):
    
    a=0
    
    newo= (newo.split(" "))
    for line in newo:
     a=a+1
     #n= (base((len(line)), 10, 10,string=True))
     #n2=len(line)+n2
     
    return (a)
def alphabet_to_num(newo):
    newo= (newo.split(" "))
    rrw2="" 

    for line in newo:
       rrw1="" 
       for line in line:  
         
         n=ord(line)
         rrw1 += str(n) + " "
       rrw2 += str(rrw1) + "/"
    #print(rrw2)  
    return (rrw2)
def addnumtogether(newo):
    rrw1=""
    rrw2=""
    rrw3=""
    rrw4=""
    a=0
    n=0
    newo= (newo.split("/"))
    for line in newo:
     line=line.split(" ")
     del line[-1:]
     for line in line:   
         n=int(line)+n
     rrw1 += str(n) + " "
     rrw2 += str(n%63) + " "
     rrw3 += str(n%127) + " "
     rrw4 += str(n%26) + " "
     n=0
    #return(rrw1,rrw2,rrw3,rrw4)
    return(rrw1) 
def addnumtogethercha(newo):
    rrw1=""
    rrw2=""
    rrw3=""
    rrw4=""
    rrw5=""
    a=0
    n=0
    newo= (newo.split("/"))
    for line in newo:
     line=line.split(" ")
     del line[-1:]
     
    
     for line2 in line:
         
         n=int(line2)+n
     rrw1 += str(n) + " "
     rrw2 += chr(n%63) + " "
     rrw3 += str(n%26+1) + " "
     rrw4 += chr(96+n%27) + " "
     rrw5 += chr(96+(n%96)%26) + " "
     n=0
    print(rrw1) 
    #print(rrw4)
    #print(rrw3)
    #print(''.join(rrw3))
    # 
    #return(rrw1,rrw2,rrw3,rrw4)
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
def len_line_to_object():
 with open('momen.txt', 'r') as file2:
    rrw1=""
    rrw2=""
    rrw3=""
    rrw4=""
    for line in file2:
        mine=(len(line))
        mine1=(len(line))-2
        mine2=(len(line))-1
        mine3=(len(line))%27        
        rrw1 += str(mine) + " "
        rrw2 += str(mine1) + " "
        rrw3 += str(mine2) + " "
        rrw4 += str(mine3) + " "
    return (rrw1,rrw2,rrw3,rrw4)
def len_line_to_object2():
 with open('dds.txt', 'r') as file2:
    rrw1=""
    rrw2=""
    rrw3=""
    rrw4=""
    for line in file2:
        mine=((len(line)))[2:]
        mine1=((len(line)))
        mine2=chr((len(line))+1)
        mine3=chr(96+(len(line)%96)%27)    
        rrw1 += str(mine) + " "
        rrw2 += str(mine1) + " "
        rrw3 += str(mine2) + " "
        rrw4 += str(mine3) + " "
    #return (rrw1,rrw2,rrw3,rrw4)    
    #print(rrw1)
    print(rrw2)
    #print(rrw3)
    #print(rrw4) 
    #pri
def null(ne):
 with open('keys.txt', 'r') as file2:
    for glp in file2:
        a=list(glp.split(" "))
        del a[-1:]
        listb=[]
        for line in ne:
            mine=line.split()
            listb=listb+[mine]
        print(listb)
    #a=[3,2,6,4,12,9,7,11,8,5,15,16,14,13,10]
        try:
            dd=0
            rrw1=[]
            for cine in a:
            
 

            
                dd=int(cine)
                
                line=listb[dd-1]
                rrw1=rrw1+line
            agt=("".join(rrw1))       
            print (agt)
        except:
            ewrewer=2
def nullplus(ne):
 with open('keys.txt', 'r') as file2:

        
  for glp in file2:
        
    a=list(glp.split(" "))
    del a[-1:]
   
    listb=[]
    for line in ne:
        mine=line.split()
        listb=listb+[mine]
    
    dd=0
    b=[]
    rrw1=[]
    
    while (len(listb)-1)>dd:
        for line in a:
            dd=dd+int(line)
            if dd<(len(listb)-1):
                b=b+[dd]
    #print(len(listb))
    try:       
     for cine in b:
            dd=cine
            line=listb[dd-1]
            rrw1=rrw1+line
     agt=("".join(rrw1))       
     return (agt)
    except:
        eeoses=2
def reorder(ne):

    ggg=[1 ,2 ,5 ,4 ,9 ,3 ,10 ,6 ,8 ,12 ,13 ,11 ,7 ,15 ,14]
    listb=[]
    for line in ne:
        mine=line.split()
        listb=listb+[mine]
    rrw1=[]
    aa=0
    while aa<15:
        
        wine=ggg[aa]
        bine=listb[wine-1]
        rrw1=rrw1+bine
        aa=aa+1
    return("".join(rrw1))

#print(word_len_to_base1033("John Napier discovered logarithms (g^x), then, in 1978,  Diffie and Hellman used a discrete method with a prime number (g^x (mod p)) to create a key exchange method ... and still in use today (but converted to ECC). But can we use any g value? Ask Sage: asecuritysite.com/sage/sage_08"))
#print(addnumtogethercha(alphabet_to_num('Hi, I’ve topped up account fuel, setup the binance api and activated trading and markets in the bot. Still no activity. Any thoughts?')))

""""
with open('momen.txt', 'r') as file1:
 for line in file1:
  needle1 = (line.strip())
  if len(needle1)>1:
      line=needle1[::-1]
      a0=vowelconstant.onlyvowel(line)
      ya0=vowelconstant.whyonlyvowel(line)
      eee=vowelconstant.baconke(a0)
      ccc=vowelconstant.baconke(ya0)
      fff=vowelconstant.reveseobin(eee)
      ggg=vowelconstant.reveseobakon(fff)
      eew=[a0,ya0,eee,ccc,fff,ggg]
      for line in eew:
          print(line)
"""          
  #newo= (needle1.split(","))
  #print (ioio(needle1))
      #print(needle1)
      #print(mod2((needle1)))
      #print(alphabet_to_num(needle1))
      #nullplus(needle1)
      #print(addnumtogether((needle1)))
      #print(addnumtogether((needle1[::-1])))
      
  
  #n= list(base(newo, 10, 2,string=True))
  #print (' '.join(n)) 
  #print (ne)
  #for hhki in (newo):
     #print (hhki)
     #print (' '.join(hhki)) 
             #for perm in list(permList): 
     #    print (''.join(perm)) 
     #a=(needle.rjust(64,'0'))
     #bb=int(a,16)
"""          
     n= list(base(hhki, 10, 7,string=True))
     
     print (' '.join(n)) 

     n= base(hhki, 10, 3,string=True)
     print (n)

     

     #gei=hex(bb)
     #c=gei[2:len(gei)]
     #a=(c.rjust(64,'0'))
     #e= c[::-1]
     #gg= needle[::-1]
     #hhki= int(gg,16)
     #print (hhki)
     n= list(base(hhki, 10, 2,string=True))
     print (' '.join(n)) 

     n= base(hhki, 10, 3,string=True)
     print (n)

     n= base(hhki, 10, 4,string=True)
     print (n)

     n= base(hhki, 10, 5,string=True)
     print (n)

     n= base(hhki, 10, 6,string=True)
     print (n)

     n= base(hhki, 10, 7,string=True)
     print (n)

     n= base(hhki, 10, 8,string=True)

     print (n)
     n= base(hhki, 10, 9,string=True)

     print (n)

"""    

        #d.write((str(gei))+ '\n')
        #c.write((pubtoaddr(compress(privtopub(eee)))+ '\n'))
        #c.write(pubtoaddr(privtopub(eee))+ '\n')
#c.close()
#d.close()


#with open('some_output_file11111888888888888888888888888888888888888888.txt', 'w') as file_out:
 #   for line in same:
        #file_out.write(line)
  #      print (line)
#close.file_out.write()

from encdecpy import *

with open('dds.txt', 'r') as file1:
 for line in file1:
      needle1 = line.strip()
  #needle2= needle1[::-1]
  #meioe=[needle1,needle2]
  #for line2 in meioe:
      print(addnumtogethercha(alphabet_to_num(line)))
      #print(((alphabet_to_num(line2))))
      #print((alphabet_to_num(line2)))
      #print(word_counrt_to_base10(needle1),end=" ")

#len_line_to_object2()
