import re
ccc = open("chiooo22222.txt", 'a')
def openfileandread(name):
   a=[]
   z=''
   with open(name, 'r') as file1:  
     for line in file1:
          needle1 = (line.strip())
          needle2=needle1.split('–')
          if len(needle2)>1:
              a=a+[str(needle2[0]).replace(' ','')]+[str(needle2[1])]
              z+=str([str(needle2[0]).replace(' ','')])
   return(a)
def osie(name):
   a=[]
   z=''
   with open(name, 'r') as file1:  
     for line in file1:
          needle1 = (line.strip())
          needle2=needle1.split('–')
          if len(needle2)>1:
              a=a+[str(needle2[0]).replace(' ','')]+[str(needle2[1])]
              z+=str([str(needle2[0]).replace(' ','')])
   return(a)
dicname='cleanfile'
dic=(openfileandread(dicname))
def dictest(string):
    k,z,n,x,fe=0,'',0,len(string),0
    evaluato=''
    info=[]
    for i in dic:
        if k%2==0:
            if i in string:
                evaluato+=i+','
                info=info+[str(i),str(dic[k+1])]
                z=z+i
                n+=1
                fe+=(len(i)**2)
        k+=1        
        if k==len(dic):
            x=((len(z)+fe))/len(string)*n
            if n>1 and x>0:
                print(x,evaluato,info)
                print(string)

def simpledict(name):
   a=[] 
   with open(name, 'r') as file1:
      for line in file1:  
        needle1 = (line.strip()).lower()
        if len(needle1)>3:
            a+=[needle1]
   return(a)
def stringtocheck(name):
    with open(name, 'r') as file1:
      for line in file1:  
        needle1 = (line.strip())
        fix=(re.sub(r'^[a-zAZ]','',needle1)).lower()
        dictest(fix)
        dictest(fix[::-1])
def simpledickchecker(string,dictu):
    z,k,m,l=' ',1,[' ',],len(string)
    for i in dictu:
        if i in string:
            z+=i
            k+=1
            m+=[i]
    if len(m)>4 and (((len(z)*k))/(len(m)*l))>0.30:
        print('source= ',string,'word= ',' '.join(m),k,((len(z)*(len(string)))/(len(m)*k)))
def filecheck(name,dictr):
    dictu=simpledict(dictr)
    with open(name,'r') as file11:
        for line in file11:
            line2=line
            line=(re.sub(r'^[a-zAZ]','',line.strip())).lower()
            #line2=
            #simpledickchecker(line,dictu)
            #simpledickchecker(line[::-1],dictu)
            for mine in dictu:
                x=[mine,mine[::-1]]
                for i in x:
                    if len(i)<len(line):
                        if line[:len(i)]==i or line[::-1][:len(i)]==i:
                            a=str(str(i)+'     string= '+str(line2))
                            ccc.write((a)+ '\n')

#dicname=simpledict('dictionary2.txt')
#filecheck('Newewe','newdic.txt')    
#dicname=simpledict('dictionary.txt')
#filecheck('milwa','cryptoname')
#dicname='testitbro32'
dicname='dictionary2.txt'
#filecheck('newmo1c.txt',dicname)
dicname=simpledict('dictionary2.txt')
#dicname=simpledict('abstract')

with open('newmo1c.txt','r') as file2:
    for i in file2:
        simpledickchecker(i.lower(),dicname)
        simpledickchecker(i.lower()[::-1],dicname)
        #dictest(i[::-1].lower())

ccc.close()
'''
source=  srmnrpnoomilroomslparsislrpsrmsrmrmnlmliolloprmmimimlntinsirsltoolut
 word=    mimi pars parsi room rooms sirs tins tool 9 29.814814814814813
source=  
tsmitilfmloomrioalirtpeiprpprlongmslnnrmipustrollermiiprsp word=    long loom roll roller stroll stroller troll 8 35.03125
source=  rsumscfvsunksmuttsutopsttucksw4stumsssnsntcskv
 word=    mutt smut sums sunk tops tuck tucks 8 22.03125
source=  gclogsodporrnnooilsissspmnsommogmrpndnaltisloopsno
 word=    clog clogs logs loop loops oils sloop 8 25.5
source=  geuhdsoamgbfpoeeomitdudclaftgfursargonropergscicd
 word=    argo argon furs omit rope roper ursa 8 24.21875
source=  gspillsrsolomlslmimsslisosinospsgitiormmsisnilmotitimmrirpnipslp
 word=    ills nips pill pills solo spill spills 8 33.515625
source=  
gspillsrsolomlslmimsslisosinospsgitiormmsisnilmcitimmrirpnipslp word=    ills nips pill pills solo spill spills 8 33.0
source=  theflowerblossomsthroughwhatseemstobeaconcretesurfa
 word=    beacon blossom blossoms concrete concretes crete flow flower hats loss lowe lower rough seem seems surf through what 19 14.404432132963988
source=  glspoolsmnplmllunoelnoprssootinsu
 word=    noel pool pools soot spool spools tins 8 17.53125
source=  theflowerblossomsthroughwhatseemstobeaconcretesurfa
 word=    beacon blossom blossoms concrete concretes crete flow flower hats loss lowe lower rough seem seems surf through what 19 14.404432132963988
source=  popillsnllimprnpisnnmomstismsnisiirtornnloorrssollsonest
 word=    ills limp nest ones pill pills torn 8 26.71875
source=  fnbephlnmsplinesslcplsssmponsoilsrnhdplprpmocmrnso
 word=    line lines ness oils soil soils spline splines 9 25.185185185185187
source=  
theflowerblossomsthroughwhatseemstobeaconcretesurface word=    beacon blossom blossoms concrete concretes crete face flow flower hats loss lowe lower rough seem seems surf surface through what 21 13.591836734693878
source=  
tpiiiidolorrommolnlssospririmsrinnsnspoolsnlmoof word=    idol inns pool pools rims spool spools 8 25.265625
source=  
thefowerbossomsthroughwhatseemstobeaconcretesurfa word=    beacon boss concrete concretes crete hats rough seem seems surf through what 13 19.526627218934912
source=  
tplossrshtlsmocorltplospurisitnrnoroarsstrposloltom word=    loss oars oslo roar roars spur uris 8 24.375
source=  
tpigssoporohpulispinspinmosrisernsnltpltmrlmlrltpplmm word=    lisp pigs pins rise riser spin spins 8 26.15625
source=  
arisenoiifimnnoonmcgittssmlsiliitssonsmlrmoroslilrlnsgilltmrlc word=    arise arisen gill noon rise risen sons 8 32.484375
source=  mopallounrrsoiirsoooironlnrsnnrnormanmolplrmmrsirlsnofmnpropiont
 word=    iron norm norma norman opal pall pion prop 9 28.88888888888889
source=  atlsosnnsrstillsohstolprprlionpsppsoomisonsmrssnplstlpm
 word=    ills lion sons still stills till tills 8 28.875
source=  
https//gsmgio/choiceisanillusioncreatedbetweenthosewithpowerandthosewithoutaveryspecialdessertiwroteitmyself word=    aver avery between choice create created dessert hose illusion myself power rand self spec special those very with without wrote 21 27.188208616780045
source=  tmodmilescfmaidnegiuhncbdapcstidescaidoorsfobdrftdgftsgo
 word=    door doors maid mile miles tide tides 8 28.5
source=  theflowerblossomsthroughwhatseemstobeaconcretesurface
 word=    beacon blossom blossoms concrete concretes crete face flow flower hats loss lowe lower rough seem seems surf surface through what 21 13.591836734693878
source=  tilimpsnoiirespsmilseimnsoonrmrimmominbrsprisnpisspit
 word=    imps ires limp limps piss soon spit 8 25.3125
source=  tisomlpnlpmplpsotliispopesmnnostlloindoorsoomorlrssftslnnmlnorlmoo
 word=    door doors indo indoor indoors loin pope 8 36.640625
source=  cmnsipastilootipssmpnpsrridsbtlilolopricoonsshlnpopogns
 word=    coon coons loot past rico rids tips 8 26.25
source=  
inalgafguoschedffttfeauntaiipmbsarprobesaatobeerh word=    alga aunt beer probe probes robe robes 8 25.78125'''