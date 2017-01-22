#import pandas as pd
#import numpy as np
#file = open('test1.txt','r')
#filewrite = open('test1_output.txt','w')
#a = 0
#for line in file:
#    a = a+1
#    values = line.split('\t')
#    b = 1
#    for value in values:
#        if(value=='1'):
#            filewrite.write(str(a) + '\t'+ str(b) + '\n')
#        b = b+1
#filewrite.close()

import pandas as pd
import numpy as np
data = pd.read_csv('test1.txt',header=None, sep = "\t")
data_matrix = np.matrix(data)
print(data_matrix.shape)
print(data_matrix.shape[0])
print(data_matrix.shape[1])

#Parse Matrix sum of each column
for i in range(0,data_matrix.shape[0]):
    sum = 0
    for j in range(0,data_matrix.shape[1]):
        sum = sum+data_matrix[i,j]
    print('row -',i+1,'-sum ',sum)

#Parse Matrix sum of each column
for i in range(0,data_matrix.shape[1]):
    sum = 0
    for j in range(0,data_matrix.shape[0]):
        sum = sum+data_matrix[j,i]
    print('column-',i+1,'-sum ',sum)

