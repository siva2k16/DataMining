import nltk
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}' ,'*','//','**'])
print(stop)
fin = open('CanonG3_untagged.txt','r', encoding='utf-8') 
fin_lower= fin.readlines()
lines=""
for line in fin_lower:
    strnouns = ""
    words = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(words)
    nouns = [word for word, pos in tagged if((pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') and (pos not in stop))]
    lowercase = [x.lower() for x in nouns]
    resultnouns = ",".join(lowercase).encode('utf-8')
    #resultnouns = resultnouns.strip('*')
    strnouns = str(resultnouns)
    strnouns_res = strnouns.replace("'*[]%*"," ")
    strnouns_res = strnouns_res.replace("b\'","")        
    strnouns_res = strnouns_res.replace("*","")
    strnouns_res = strnouns_res.replace("[","")
    strnouns_res = strnouns_res.replace("]","")
    strnouns_res = strnouns_res.replace("%","")
    strnouns_res = strnouns_res.replace("/","")
    strnouns_res = strnouns_res.replace("'","")     
    if(len(strnouns_res)>0):
        strnouns_res = strnouns_res.replace(",,",",") 
        #strnouns = str("["+resultnouns+"],")
        print('Nouns Identified')
        print('=================')
        print(strnouns_res)
        output = open("Nouns_Results_2A.txt","a")
        output.write(strnouns_res)
        output.write("\n")
        output.close()
fin.close()

