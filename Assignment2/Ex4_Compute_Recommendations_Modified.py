import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

shownames = pd.read_csv('shows.txt',header=None)
data = pd.read_csv('user-shows.txt',header=None, sep = " ")
data_matrix = np.matrix(data)
print(data_matrix.shape)
print(data_matrix.shape[0])
print(data_matrix.shape[1])

def Compute(data_matrix):
    Rmatrix = data_matrix
    RTranspose = np.transpose(Rmatrix)
    #Compute Q
    Q = []
    #Parse Columns
    for i in range(0,data_matrix.shape[1]):
        sum = 0
        for j in range(0,data_matrix.shape[0]):
            sum = sum+data_matrix[j,i]
        Q.append(1/np.sqrt(sum))
    #Compute Diagonal Matrix
    #Compute P
    P = []
    #Parse Columns
    for i in range(0,data_matrix.shape[0]):
        sum = 0
        for j in range(0,data_matrix.shape[1]):
            sum = sum+data_matrix[i,j]
        P.append(1/np.sqrt(sum))

    Qmatrix = np.diagflat(Q)
    Pmatrix = np.diagflat(P)
    print(Qmatrix.shape)
    print(Pmatrix.shape)
    #Compute Diagonal Matrix
    #Compute SU
    #User Item Filtering
    SI = Qmatrix*RTranspose*Rmatrix*Qmatrix
    print('SU')
    print(SI.shape)
    #Compute SI
    #Item-Item Filtering
    SU = Pmatrix*Rmatrix*RTranspose*Pmatrix
    print('SU')
    print(SU.shape)
    #UserItemRating
    DovUUrating = SU*Rmatrix
    DovIIrating = Rmatrix*SI
    return DovUUrating, DovIIrating

#Invoke Function
DovUUrating, DovIIrating = Compute(data_matrix)

def ComputeTop20Results(DovUUrating, DovIIrating):
    #Dictionary of values
    #Fetch the 20th row 100 columns with Index into a variable
    uuresult = {}
    #print('User-User Rating')
    for j in range(0,100):
        uuresult[j] = DovUUrating[19,j]
        #print(DovUUrating[20,j])
    iiresults = {}
    #print('Item-Item Rating')    
    for j in range(0,100):
        iiresults[j] = DovIIrating[19,j]
        #print(DovIIrating[20,j])    
    #print('UU')
    uupositions = []
    uuvalues = []
    uuresultresorted = sorted(uuresult, key=uuresult.get, reverse=True)
    for i in range(0,20):
        #print(uuresultresorted[i])
        uupositions.append(uuresultresorted[i])
        #print(uuresult.get(uuresultresorted[i]))
        uuvalues.append(uuresult.get(uuresultresorted[i]))
    #print(uuresultresorted)
    iipositions = []
    iivalues = []
    iiresultssorted =  sorted(iiresults, key=iiresults.get, reverse=True)
    #print(iiresultssorted)
    for i in range(0,20):
        #print(iiresultssorted[i])
        iipositions.append(iiresultssorted[i])
        #print(iiresults.get(iiresultssorted[i]))
        iivalues.append(iiresults.get(iiresultssorted[i]))
    return iivalues, uuvalues, iipositions, uupositions

iivalues, uuvalues, iipositions, uupositions= ComputeTop20Results(DovUUrating, DovIIrating)
print(iipositions)

actualratings = []

#Initiakize R to Zeros
#Invoke the function
for i in range(0,100):
    if(data_matrix[19,i] == 1):
        actualratings.append(i)
    data_matrix[19,i] = 0

print('actualratings')
print(actualratings)
    
DovModifiedUUrating, DovModifiedIIrating = Compute(data_matrix)
    
iimodifiedvalues, uumodifiedvalues, iimodifiedpositions, uumodifiedpositions= ComputeTop20Results(DovModifiedUUrating, DovModifiedIIrating)
print(iimodifiedpositions)
print(iipositions)

b = iimodifiedpositions[:5]
a = uumodifiedpositions[:5]
c = uumodifiedpositions[:10]
d = iimodifiedpositions[:10]

print('Item Item Recommendations')
print(shownames.ix[b])
print('User User Recommendations')
print(shownames.ix[a])

#for top 1..19
#plt.figure(1)
plt.figure()
for i in range(1,20):
    tp = 0.0
    a = []
    a = actualratings
    #print('a',a)
    b = []
    b = iimodifiedpositions[:i]
    #print('b',b)
    fp = len((set(a).intersection(set(b))))
    tp = fp/19
    print('i-',i,'-tp',tp, '-fp',fp)
    plt.plot(i,tp,'o',color='g')

for i in range(1,20):
    tp = 0.0
    a = []
    a = actualratings
    #print('a',a)
    b = []
    b = uumodifiedpositions[:i]
    #print('b',b)
    fp = len((set(a).intersection(set(b))))
    tp = fp/19
    print('i-',i,'-tp',tp, '-fp',fp)
    plt.plot(i,tp,'o',color='r')
    plt.title("Red - user to user / Green - Item to Item")
plt.show()

print('User User Top 10 Recommendations')
print(shownames.ix[c])

print('Item Item Top 10 Recommendations')
print(shownames.ix[d])

