from scipy import stats
aUU = [96, 74, 140, 45, 60, 156, 68, 35, 137, 326]
bII = [144, 96, 35, 74, 155, 173, 205, 63, 140, 145]
cWRMF = [48, 77, 192, 208, 280, 195, 207, 222, 219, 489]
dKNN = [234, 48, 37, 543, 490, 477, 280, 553, 489, 222]

def computestats(a,b):
    tau, p_value = stats.kendalltau(a, b)
    return tau, p_value
    
tau, p_value = computestats(aUU,aUU)
print(tau)

tau, p_value = computestats(aUU,bII)
print(tau)

tau, p_value = computestats(aUU,cWRMF)
print(tau)

tau, p_value = computestats(aUU,dKNN)
print(tau)

tau, p_value = computestats(bII,aUU)
print(tau)

tau, p_value = computestats(bII,bII)
print(tau)

tau, p_value = computestats(bII,cWRMF)
print(tau)

tau, p_value = computestats(bII,dKNN)
print(tau)

tau, p_value = computestats(cWRMF,aUU)
print(tau)

tau, p_value = computestats(cWRMF,bII)
print(tau)

tau, p_value = computestats(cWRMF,cWRMF)
print(tau)

tau, p_value = computestats(cWRMF,dKNN)
print(tau)

tau, p_value = computestats(dKNN,aUU)
print(tau)

tau, p_value = computestats(dKNN,bII)
print(tau)

tau, p_value = computestats(dKNN,cWRMF)
print(tau)

tau, p_value = computestats(dKNN,dKNN)
print(tau)

