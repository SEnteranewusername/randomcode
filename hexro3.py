# /usr/bin/pypy
#from bitcoin import *
#ccc = open('comp.txt', 'w')
import re
bbb = open('moplll.txt', 'w')
#eee = open('up3333.txt', 'w')
nnn = 115792089237316195423570985008687907852837564279074904382605163141518161494337
def ascii128(hexstring):
    try:
        
     a121212=(bytes.fromhex(hexstring))
     b212121212=a121212.decode("ascii")
     return (b212121212)
    except:
         pass

#print(b)
def revwordstring(rowhexstr):
 #a_string=rowhexstr.rjust(64,"0")
 split_strings = []
 n=2
 byterevdone=""
 for index in range(0, len(rowhexstr), n):
     split_strings.append(rowhexstr[index : index + n])
     byterevdone=''.join(reversed(split_strings))
     
     #reverse_sentence = ' '.join(reversed(words)) 
 return (byterevdone)
with open('mioeo.txt', 'r') as file1:

 for line in file1:
        #needle=hex(int(line.strip()))[2:]
             

            

              needle=line.strip()
              #needle=((hex(int(needlew,2)))[2:])
              #needle = int((line.strip()),16)
              #needle=(line.strip()).ljust(64,"B")
              #needle=  (hex((int(needle))%nnn))[2:]
              rev= (str(needle))[::-1]
              revwordstringrevhex=revwordstring(needle)
              revwordstringhexrev=revwordstring(rev)

#,rev,revwordstringrevhex,
              fefe= (needle,revwordstringhexrev,rev,revwordstringrevhex)
              for line in fefe:
                    
                      #x = re.findall("2aa7a99", line)
                      #if len(x)>0:

                          #bbb.write(str((line)+ '\n'))
                      bbb.write(str((line)+ '\n'))
                      #bbb.write(str(line,16)+ '\n'))

#ccc.close()
bbb.close()
#eee.close()

    