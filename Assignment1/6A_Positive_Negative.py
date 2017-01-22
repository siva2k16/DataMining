
#Load Exercise Output
#Frequently occuring words
fin = open('Adverbs_Results.txt','r')
fin_lower= fin.readlines()
lines=""
adverbresults = [];
print('Result')
for line in fin_lower:
    words = line.split(',')
    for word in words:
        word = word.strip()
        CorrectedString = ""
        for characters in word:
            if characters.isalpha():
                CorrectedString += characters
        if(CorrectedString not in adverbresults):
            adverbresults.append(CorrectedString)
print(adverbresults)

#Load positive words
fin = open('positive-words.txt','r')
fin_lower= fin.readlines()
lines=""
positivewordresults = [];
print('Result')
for line in fin_lower:
    words = line.split(',')
    for word in words:
        word = word.strip()
        CorrectedString = ""
        for characters in word:
            if characters.isalpha():
                CorrectedString += characters
        if(CorrectedString not in positivewordresults):
            positivewordresults.append(CorrectedString)

print(positivewordresults)

#Load Negative words
fin = open('negative-words.txt','r')
fin_lower= fin.readlines()
lines=""
negativewordresults = [];
print('Result')
for line in fin_lower:
    words = line.split(',')
    for word in words:
        word = word.strip()
        CorrectedString = ""
        for characters in word:
            if characters.isalpha():
                CorrectedString += characters
        if(CorrectedString not in negativewordresults):
            negativewordresults.append(CorrectedString)

print(negativewordresults)

#print count positive
print(len(positivewordresults))
#print count negative
print(len(negativewordresults))

count = 0
for x in positivewordresults:
    if x in adverbresults:
        count = count+1
positiveword = count
print('positiveword -', positiveword)

count = 0
for x in negativewordresults:
    if x in adverbresults:
        count = count+1
negativeword = count
print('negativeword -', negativeword)

#print count positive
print('Opinionwords',len(adverbresults))
