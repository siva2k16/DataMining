import nltk
from nltk.corpus import stopwords
from ast import literal_eval
import re

#Frequently occuring words
fin = open('Result_apriori_2.txt','r')
fin_lower= fin.readlines()
lines=""
results = [];
print('Result')
for line in fin_lower:
    line.encode("utf-8")
    result = re.findall(r"['\"](.*?)['\"]", line)
    results.append(result)
    
my_lst_str = ','.join(map(str, results))
my_lst_str = re.sub('[^A-Za-z0-9]+', ',', my_lst_str)
result = my_lst_str.split(',')
print(result)

output = open("Apriori_Result_Features_1.txt","a")
strresult = str(result)
strresult = strresult.replace('[','')
strresult = strresult.replace(']','')
output.write(strresult)
output.write("\n")
output.close()                     

stop = set(stopwords.words('english'))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}' ,'*','//','**'])
fin = open('CanonG3_untagged.txt','r')
fin_lower= fin.readlines()
lines=""

for line in fin_lower:
    strnouns = ""
    words = nltk.word_tokenize(line)
    if any(s in line for s in result):
        tagged = nltk.pos_tag(words)
        AdjAdv = [word for word, pos in tagged if((pos == 'JJR' or pos == 'JJ' or pos == 'JJS' or pos == 'RB' or pos == 'RBR' or pos == 'RBS' ) and (pos not in stop))]
        lowercase = [x.lower() for x in AdjAdv]
        resultAdjAdv = ",".join(lowercase).encode('utf-8')
        strnouns = str(resultAdjAdv)
        strnouns = strnouns.replace('\"','')
        strnouns = strnouns.replace('*','')
        strnouns = strnouns.replace('b\'','')
        strnouns = strnouns.replace('\'','')   
        strnouns = strnouns.replace('/','')         
        strnouns = strnouns.replace(']','')
        strnouns = strnouns.replace('[','')    
        strnouns = strnouns.replace('+','')    
        strnouns = strnouns.replace(',,',',')
        strnouns = strnouns.replace(' ,','')  
        strnouns = strnouns.strip()         
        #resultAdjAdv = resultAdjAdv.strip('*')
        print(strnouns)
        if(len(strnouns)>0):
            print('Adverbs Identified')
            print('=================')
            print(strnouns)
            output = open("Adverbs_Results.txt","a")
            output.write(strnouns)
            output.write("\n")
            output.close()
fin.close()
