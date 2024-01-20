from encdecpy import *
import nullCipher, pyperclip, detectEnglish, itertools
with open('decidemy.txt', 'r') as file1:
 for line in file1:
  needle1 = (line.strip())
  needle2= needle1[::-1]
  meioe=[needle1,needle2]
  for line3 in meioe:
      if detectEnglish.isEnglish(line3):
          print(line3)