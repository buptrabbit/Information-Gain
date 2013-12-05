import math

def get_pc(inputpath):
    cnt_c = [0]*33
    dic = {}
    clsList = ['']*33
    for line in open(inputpath):
        line,cls = line.rstrip('\n').rsplit('\t',1)
        cnt_c[int(cls)-1] += 1
        clsList[int(cls)-1] += (line+'\t')
    Dtotal = float(sum(cnt_c))
    for i in range(33):
        dic[i+1] = [cnt_c[i],cnt_c[i]/Dtotal]
    pc = [v for [k,v] in dic.values()]
    Hc = -sum([(lambda p: p*math.log(p,2))(p) for p in pc])
    return Hc,Dtotal,clsList,cnt_c

def gen_ig(Hc,Dtotal,clsList,cnt_c):
    dic = {}
    dic_ig = {}
    for i in range(33):
        lst = clsList[i].split('\t')
        for l in lst:
            d = jieba.analyse.extract_tags(l,2)
            for k in d.keys():
                if fltr(k):
                    continue
                if dic.has_key(k):
                    dic[k][i] += 1
                else:
                    dic[k] = [0]*33
                    dic[k][i] += 1
    for k in dic.keys():
        pt = sum(dic[k])/Dtotal
        pc_t = [nc/float(sum(dic[k])) for nc in dic[k]]
        pc_t_ = [(nc-nct)/(Dtotal-float(sum(dic[k]))) for (nc,nct) in zip(cnt_c,dic[k])]
        dic_ig[k] = Hc+pt*sum([(lambda p: p*math.log(p,2))(p) for p in pc_t if not p==0])+(1-pt)*sum([(lambda p: p*math.log(p,2))(p) for p in pc_t_ if not p==0])
    return dic_ig
