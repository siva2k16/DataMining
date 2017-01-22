import nltk
from nltk.corpus import stopwords
from ast import literal_eval
import re

#Frequently occuring words
fin = open('Apriori_Result_Features_1.txt','r')
fin_lower= fin.readlines()
lines=""
results = [];
print('Result')
for line in fin_lower:
    words = line.split(',')
    for word in words:
        word = word.strip()
        CorrectedString = ""
        for characters in word:
            if characters.isalpha():
                CorrectedString += characters
        if(CorrectedString not in results):
            results.append(CorrectedString)
            print(CorrectedString)
            output = open("UnTagged_Features.txt","a")
            output.write(CorrectedString)
            output.write("\n")
            output.close()                     
