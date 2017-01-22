import re
#File 1
#File 2
File1 = open("Tagged_Features.txt","r")
File2 = open("UnTagged_Features.txt","r")
Dict1 = File1.readlines()
Dict2 = File2.readlines()

File1String = []
File2String = []

for line in Dict1:
        line = line.strip()    
        line = re.sub('\(\)', '', line)
        words = line.split(',')
        if(len(line)>0):
            for word in words:
                word = word.strip()
                word = word.replace('(',"")
                word = word.replace(')',"")
                if(word not in File1String):
                    File1String.append(word)
            
print('File1', len(File1String))
print(File1String)

for line in Dict2:
        line = line.strip()
        words = line.split(',')
        if(len(line)>0):
            for word in words:
                word = word.replace('\'','')
                word = word.strip()
                if(word not in File2String):
                    File2String.append(word)
                    
print('File2',len(File2String))
print(File2String)

count = 0
for x in File1String:
    if x in File2String:
        count = count+1
tp = count
print('Common count two lists (TP) -', tp)

count = 0
for x in File1String:
    if x not in File2String:
        count = count+1
fn = count
print('Tagged_Features - UnTagged (Fn) -', fn)

count = 0
for x in File2String:
    if x not in File1String:
        count = count+1
fp = count
print('UnTagged -Tagged_Features (Fp) -', fp)

precision = 0.0
recall = 0.0

precision = float((tp)/(tp+fp))
recall = float((tp)/(tp+fn))

print('precision', precision)
print('recall', recall)

f1score = 0.0
f1score = (2*recall*precision)/(precision+recall)
print('f1score', f1score)

