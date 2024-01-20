import re
c25 = open('Step2.txt', 'w')
#from itertools import combinations
#comb = combinations(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"], 2)
def baconke(line):
    lista=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for i in lista:
      c25.write((((re.sub('B', i, line))))+"\n")

with open('Stepone.txt', 'r') as file1:
     for line in file1:
       baconke(line.strip())
c25.close()