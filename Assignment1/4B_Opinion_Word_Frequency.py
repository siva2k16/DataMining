import re
import collections
words = re.findall('\w+', open('Adverbs_Results.txt').read().lower())
print(collections.Counter(words))
output = open("Adverbs_Counts_Results_4A.txt","a")
output.write(str(collections.Counter(words)))
output.close()