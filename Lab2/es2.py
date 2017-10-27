import re

def freq(file):
    d=dict()
    f=open(file)
    for i in f:
        i=re.sub("[,;.:?!\'\"«»’]"," ",i)
        words = i.lower().split()
        for j in words:
            if(j in d):
                d[j]+=1
            else:
                d[j]=1
    l=sorted([(v,k) for k,v in d.items()],reverse=1)
    for i in l:
        print("{0}: {1}".format(i[1],i[0]))
    return l
