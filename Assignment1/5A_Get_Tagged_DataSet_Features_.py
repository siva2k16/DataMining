import nltk
from nltk.corpus import stopwords
from ast import literal_eval
import re

stop = set(stopwords.words('english'))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}' ,'*','//','**'])
fin = open('CanonG3_tagged.txt','r')
fin_lower= fin.readlines()
lines=""

for line in fin_lower:
    strnouns = ""
    if(('[+' in line) or ('[-' in line)):
        words = line.split('##')
        for word in words:
             if('[' in word and '[t]' not in word):
                 #print(word)
                 features = word.split(',')
                 for feature in features:
                     feature = feature.strip() 
                     output = re.sub('[0-9]+', '', feature)
                     output = output.replace('+','')
                     output = output.replace('-','')
                     output = output.replace('[','')
                     output = output.replace(']','')
                     output = output.replace('{','')
                     output = output.replace('}','')  
                     print(output)
                     strresult = str(output)
                     output = open("Tagged_Features.txt","a")
                     output.write(strresult)
                     output.write("\n")
                     output.close()                     
