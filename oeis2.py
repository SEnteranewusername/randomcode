import re
def simpledict(name):
   a=[] 
   with open(name, 'r') as file1:
      #z=0 
      for line in file1:  
        needle1 = (line.strip()).lower()[::-1]
        #z+=1
        if len(needle1)>3:
            a+=[needle1]
   return(a)
def faster(name):
    z=''
    with open(name, 'r') as file1:
        for line in file1:
            z+=line.strip().replace(' ','').lower()
    return(z)
oeis=faster('names')
wordto=simpledict('dic')
def testarrange(fr,to):
    x=[]
    for i in fr:
        x+=[[len(re.findall(i,to)),i]]
    x.sort(key=lambda x: x[0],reverse=True)
    #x.sort(reverse=True)
    #print(x[0:10])
    return(x)
stre='The smallest act of kindness is worth more than the grandest intention oscar wilde'.lower().split(' ')
#for i in testarrange(stre,oeis):
#                print(i)
def openfile(name):
    namelist,ls=[],''
    with open(name,'r') as file:
        for line in file:
            ls+=line.strip().lower()
        
    ls.replace('  ',' ')
    for i in ls.split(' '):
       if i not in namelist:
           
           if len(i)>3:
            namelist+=[(re.sub(r'[^a-z]','',i))[::-1]]
    #ls=re.sub(r'[a-z]','',ls)    
    return(ls,namelist)
def doublecheck(name):
    filin=openfile(name)
    for i in testarrange(filin[1],oeis):
        print(i)
#doublecheck('New')
#z=openfile('New')[1]
#for i in z: print(i)


'''
with open ('New4','r') as file:
    ze=''
    for line in file:
        for i in line:
           if ord(i)<33 or ord(i)>127:
              if ord(i)==10:
                  ze+='0'
              elif ord(i)==32:
                  ze+='1'
              elif ord(i)==9:
                  #print(i)
                  ze+=''
print(ze)
'''              
    #print(ze)
    
#its so annoying!             
'''Traceback (most recent call last):
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/oeis.py", line 29, in <module>
    for i in testarrange(line,oeis):
NameError: name 'line' is not defined
>>> %Run oeis.py
Traceback (most recent call last):
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/oeis.py", line 46, in <module>
    doublecheck('New')
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/oeis.py", line 44, in doublecheck
    filin=openfile(name)
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/oeis.py", line 32, in openfile
    namelist,ls=[],ls
UnboundLocalError: local variable 'ls' referenced before assignment
>>> %Run oeis.py
Traceback (most recent call last):
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/oeis.py", line 46, in <module>
    doublecheck('New')
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/oeis.py", line 45, in doublecheck
    testarrange(filin[1],oeis)
  File "/media/panther/53659f40-91e7-4cb5-a883-fcadc1c8dc94/panther/tools/pro/codebreaker-master/codebreaker-master/numberseqounce/oeis.py", line 23, in testarrange
    x+=[[len(re.findall(i,to)),i]]
  File "/usr/lib/python3.6/re.py", line 222, in findall
    return _compile(pattern, flags).findall(string)
  File "/usr/lib/python3.6/re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.6/sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.6/sre_parse.py", line 855, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.6/sre_parse.py", line 416, in _parse_sub
    not nested and not items))
  File "/usr/lib/python3.6/sre_parse.py", line 768, in _parse
    source.tell() - start)
sre_constants.error: missing ), unterminated subpattern at position 0'''
#wow! its intersting.
zws=''
with open('New','r') as file:
    for line in file:
        zws+=line.strip()
zee=re.sub(r'[^a-z]','',zws)
mwe=re.sub(r'[aoiyue]','1',zee)
mwe=re.sub(r'[a-z]','0',mwe)
#print(mwe)
zws=[chr for chr in zws]
zws.sort()
print(zws)
#another intersting.
#... Y was awosmoe.
#i shou
#but why? the... is?> its means multple decryption for example where one is backon one is ook and the exact is about string