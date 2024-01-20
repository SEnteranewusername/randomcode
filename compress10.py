#!/usr/bin/env pypy
from bitcoin import *
nnn = 115792089237316195423570985008687907852837564279074904382605163141518161494337
import csv
pcsvallh=open('upcsvallhweeeeeee.csv', 'w')
writers=csv.writer(pcsvallh)
#e = open('fileoooooooooooooooooop.txt', 'w')
cccc = open('keyso01weeeee.txt', 'w')
def ignorethis(x):
        P = 2**256 - 2**32 - 977
        
        
        beta = pow(int(x*x*x+7), int((P+1)//4), int(P))
        y = (P-beta)
        return (y,beta)
with open("keyfor2.txt") as f:
    for line  in f:

      needle=line.strip()
      needle2=int(needle,16)%nnn
      needle3=(needle2-nnn)%nnn
      se=[needle2,needle3]
      for pide in se:
        cee=0  
        a1=privtopub(pide)
        while cee<1033:
            
            x=a1[0]
            x=x+cee
            x1=x-cee
            cee=cee+1
            mix=[x,x1]
            for need in mix:
                c=ignorethis(need)
                for needle01 in c:
                    needle1=int(needle01)
                    aaa=str(pubtoaddr(compress(privtopub(needle1))))
                    bbb=str(pubtoaddr(privtopub(needle1)))
                    
                    cccc.write(str(aaa)+ '\n')
                    cccc.write(str(bbb)+ '\n')
                    cip=[hex(int(needle1))]+[str((aaa))]+[str((bbb))]+[str((needle1))]
                    writers.writerow(cip)
                    cipe=((" ".join(cip)))
                    pcsvallh.write((cipe)+ '\n')


##c.close()
cccc.close()
pcsvallh.close()