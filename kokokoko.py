nnn=115792089237316195423570985008687907852837564279074904382605163141518161494337
from bitcoin import *
#print (decompress("0200da3994e2e3127562c5c5985905aee8adcab095c868ce42642707ffc006497d"))
#print (encode_privkey(bb,"wif", vbyte=0))
def revwordstring(rowhexstr):
 #a_string=rowhexstr.rjust(64,"0")
 split_strings = []
 n=2
 for index in range(0, len(rowhexstr), n):
     split_strings.append(rowhexstr[index : index + n])
     byterevdone=''.join(reversed(split_strings))
     
     #reverse_sentence = ' '.join(reversed(words)) 
 return (byterevdone)
ccc = open('mekaooo60.txt', 'a')
eee = open('bekaoo0.txt', 'a')
with open("ketest") as f:
    for needle3d in f:
     try:   
      needle0=((int(needle3d.strip()[::-1],16)))
##      needle0=int(needle3d.strip())
      a=1
      sd=privkey_to_pubkey(needle3d[::-1].rjust(64,'0'))
      
      se=int(sd[2:66],16)
      sf=int(sd[66:],16)
      needleee=[needle0,se,sf]
      for needle1 in needleee:
          

      


     #if len(needle22)<65:
     #needle08=needle22[::-1]
     #if len(needle22)>65:
     #needle081=needle22[2:]
     #needle082=needle22[:-2]
     #mweew=[needle08,needle081,needle082]
     #for line in mweew:
        
     #else:
         #needle0=needle22
        #needle=(needle3d.strip())
        #needle=((hex(int(needle)))[2:]).rjust(64,"0")
        needle1=int(needle1)
        try:
            

            
           
            #nnn1=neg_pubkey(nn1)
            #needle1=privkey_to_pubkey(needle)
            #print(decompress("032fa1bb2219601a6904afc18445dc0573abebdfa0da5f89c52e766d3ed518cb2b"))
            #needle1=neg_pubkey(line)

                #print ((pubtoaddr(compress((i)))))
                #print ((pubtoaddr((i))))

            while a<1032:
                
                
                aa=privkey_to_pubkey((hex(a+needle1))[2:])
                
                aa2=privkey_to_pubkey((hex((a*needle1)%nnn))[2:])

                aa3=privkey_to_pubkey((hex((needle1-a)%nnn))[2:])
                
                powa=pow(a,nnn-2,nnn)
                aa4=privkey_to_pubkey((hex((needle1*powa)%nnn))[2:])
                
               

                #pv=str(needle+a)
                #eee.write((pv)+ '\n')
                a=a+1
                
                gggg= (aa,aa2,aa3,aa4)
                for i in gggg:
##                    print((( ((pubtoaddr(compress((i))))))))
##                    print(( ((pubtoaddr(((i)))))))
                    ccc.write(str(needle1)+ '\n')
                    ccc.write(str(i[2:66])+ '\n')
                    
                    ccc.write((pubtoaddr(compress((i))))+ '\n')
                    ccc.write(( ((pubtoaddr((i)))))+ '\n')
                    
                    #pv=str(i)
                    #print(i[2:66])
                    
                   # print ((pubtoaddr(compress((i)))))
                    #print ((pubtoaddr((i))))
        except:
            ew=2
     except:
         ewerwewerwer=2
ccc.close()
eee.close()
#print (encode_privkey(bb,"wif_compressed", vbyte=0))

#a=privkey_to_address("KwDiBf89QgGbjEhKnhXJuH7cbeG5y4PFJ6qZMpHdQC9wVhg4t5rs")
#a=(pubtoaddr(privtopub("5HwoXVkHoRM8sL2KmNRS217n1g8mPPBomrY7yehCuXC1115WWsh")))
#print ((pubtoaddr(compress(privtopub(a)))))