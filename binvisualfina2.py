
cinama = open('nosin.txt', 'w')

def left2right(bin_result): 
 wordlist = ""
 a=0
 i=0
 indexnum=0
 stringbin=""
 split_string = [bin_result[i:i+8] for i in range(0, len(bin_result), 8)]
    #print(bin_result[i*11 : (i+1)*11])
 for i in split_string:
     
     if indexnum%2==0:
     
         stringbin=split_string[indexnum]
     
     if (indexnum%2)>0:
        stringbin=(split_string[indexnum])[::-1]
     #print (index)
        
    
     wordlist += (stringbin)+ ""
     
     indexnum=indexnum+1
     #ewew=inlist(index)
    #print(str(index)) #inlist(index_list[index])
 return (wordlist)
def right2left(bin_result): 
 wordlist = ""
 a=0
 i=0
 indexnum=0
 stringbin=""
 split_string = [bin_result[i:i+16] for i in range(0, 256, 16)]
    #print(bin_result[i*11 : (i+1)*11])
 for i in split_string:
     
     if indexnum%2==0:
     
         
        stringbin=(split_string[indexnum])[::-1]
     if (indexnum%2)>0:
        
     #print (index)
        stringbin=split_string[indexnum]
        
    
     wordlist += (stringbin)+ ""
     
     indexnum=indexnum+1
     #ewew=inlist(index)
    #print(str(index)) #inlist(index_list[index])
 return (wordlist)

def turn2right(bin_result): 
 wordlist = ""
 wordlist2 = ""
 a=0
 i=0
 indexnum=0
 stringbin=""
 plus=0
 bin_result=bin_result.split()
 for line in bin_result:
     
     #print (line[0])
     while plus<16:
         i=plus
         plus=plus+1
         while i<=255:
             
             line2=line[i]
             i=i+16
             #print (i)
             wordlist += (line2)+ ""
         #print (wordlist)
     wordlist2 += (wordlist)+ ""
 return (wordlist2)

def turn2left(bin_result): 
 wordlist = ""
 wordlist2 = ""
 a=0
 i=0
 indexnum=0
 stringbin=""
 plus=15
 bin_result=bin_result.split()
 for line in bin_result:
     
     #print (line[0])
     while plus>-1:
         i=plus
         plus=plus-1
         while i>=255:
             
             line2=line[abs(i)]
             i=i*16
             #print (i)
             wordlist += (line2)+ ""
         #print (wordlist)
     wordlist2 += (wordlist)+ ""
 return (wordlist2)
 
def rotatezip(bin_result): 
 wordlist = ""

 i=0
 indexnum=0

 split_string = [bin_result[i:i+16] for i in range(0, 256, 16)]
 bin_resulturnrp=list(zip(*split_string))[::-1]

 for line in bin_resulturnrp:

   for line in line:

     wordlist += (line)+ ""

 return (wordlist)    
def mirrorvertical(bin_result): 
 wordlist = ""
 a=0
 i=0
 indexnum=0
 stringbin=""
 split_string = [bin_result[i:i+16] for i in range(0, 256, 16)]
 for i in split_string:

     stringbin=(split_string[indexnum])[::-1]
     wordlist += (stringbin)+ ""
     
     indexnum=indexnum+1

 return (wordlist)
def mirrorhorzental(bin_result): 
 wordlist = ""

 i=0
 indexnum=0

 split_string = [bin_result[i:i+16] for i in range(0, 256, 16)]
 bin_resulturnrp=list(zip(*split_string))

 for line in bin_resulturnrp:

   for line in line:

     wordlist += (line)+ ""

 return (wordlist)
def hexit(bin_result):
    simple=(hex(int(bin_result,2)))[2:]
    return (simple)
def hexint(bin_result):
    simple=(hex(int(bin_result)))[2:]
    return (simple)
def teste(a):
    #for line in a:
       c=int(a,2)
       #c2= np.binary_repr(c, width=1802)
       #c=c[2:len(c)]
       return c
vector=teste("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")    
with open('lokerdar.txt') as source:
   eachline=""
   
   for line in source:
     eachline=""
     aa=0
     line=bin(int(line.strip(),16))[2:]
     if len(line)<257:
      line0=(line.rjust(256,"0"))[::-1]
      line1=(line.ljust(256,"0"))[::-1]
      line2=(line.rjust(256,"0"))
      line3=(line.ljust(256,"0"))
      allline=(line0, line1,line2,line3)
      for line in allline:
         line=(line.strip())
         bin_resulturnr0=rotatezip(line)
         bin_resulturnr1=rotatezip(bin_resulturnr0)
         bin_resulturnr2=rotatezip(bin_resulturnr1)
         
         collectionbrute=(line,bin_resulturnr0,bin_resulturnr1,bin_resulturnr2)
         for line in collectionbrute:
             line=line.strip()
             mirrorverl=(mirrorvertical(line))
             mirrorhorz=(mirrorhorzental(line))
             mirrormirror=mirrorhorzental(mirrorverl)
             collectionbrutesemifinal=(line,mirrorverl,mirrorhorz,mirrormirror)
             for line2 in collectionbrutesemifinal:
             #mirrorvertical=hexit(mirrorvertical(line))
                 line3=line2.strip()
                 left2ri =(left2right(line3))
                 right2le = (right2left(line3))
                 collectionfinal=(line3,left2ri,right2le)
                 for line4 in collectionfinal:
                     line5=hexit(line4)
                     xorready=teste(line4)
                     xorfi=hexint(xorready^vector)
                     #print (line5)
                     cinama.write(((line5))+ '\n')
                     cinama.write(((xorfi))+ '\n')
cinama.close()
             
