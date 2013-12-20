import math

def info_gain(x,y,k=None):
    num_d = len(y)
    num_ck = {}
    num_fi_ck = {}
    num_nfi_ck = {}
    for xi,yi in zip(x,y):
        num_ck[yi] = num_ck.get(yi,0)+1
        for index,xii in enumerate(xi):
            if not num_fi_ck.has_key(index):
                num_fi_ck[index] = {}
                num_nfi_ck[index] = {}    
            if not num_fi_ck[index].has_key(yi):
                num_fi_ck[index][yi] = 0
                num_nfi_ck[index][yi] = 0
            if not xii==0:
                num_fi_ck[index][yi] = num_fi_ck[index].get(yi)+1
            else:
                num_nfi_ck[index][yi] = num_nfi_ck[index].get(yi)+1
    num_fi = {}
    for fi,dic in num_fi_ck.items():
        num_fi[fi] = sum(dic.values())
    num_nfi = dict([(fi,num_d-num) for fi,num in num_fi.items()])
    HD = 0
    for ck,num in num_ck.items():
        p = float(num)/num_d
        HD = HD-p*math.log(p,2)
    IG = {}
    for fi in num_fi_ck.keys():
        POS = 0
        for yi,num in num_fi_ck[fi].items():
            p = (float(num)+0.0001)/(num_fi[fi]+0.0001*len(dic))
            POS = POS - p*math.log(p,2)
        
        NEG = 0
        for yi,num in num_nfi_ck[fi].items():
            p = (float(num)+0.0001)/(num_nfi[fi]+0.0001*len(dic))
            NEG = NEG - p*math.log(p,2)
        p = float(num_fi[fi])/num_d
        IG[fi] = round(HD - p*POS - (1-p)*NEG,4)
    IG = sorted(IG.items(),key=lambda d:d[1],reverse=True)
    if k==None:
        return IG
    else:
        return IG[0:k]

def red(x,IG):
    feature = dict.fromkeys([fi for fi,v in IG])
    newx = []
    for xi in x:
        newrow = []
        for index,xii in enumerate(xi):
            if feature.has_key(index):
                newrow.append(xii)
        newx.append(newrow)
    return newx
#test
'''
x = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,1,0,0]]
y = [1,2,3,2,2]
IG = info_gain(x,y,2)
for k,v in IG:
    print k,v
'''
