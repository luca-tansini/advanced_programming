def findngramsinword(word,ngramlen,dictionary):
    for i in range(0,1+len(word)-ngramlen):
        ngram = word[i:i+ngramlen]
        if(dictionary.get(ngram)): dictionary[ngram] += 1
        else: dictionary[ngram] = 1

def isword(str):
    for w in str:
        if(not('A' <= w <= 'Z' or 'a' <= w <= 'z' or '0' <= w <= '9')): return False
    return True

def sortdict(d):
    return sorted(d.items(), key = lambda tuple: tuple[1])[-1:0:-1]

def findngramsintext(textfile,ngramlen):
    d = dict()
    for i in open(textfile):
        j = i.split(' ')
        for i in j:
            if(isword(i)): findngramsinword(i.lower(),ngramlen,d)
    return sortdict(d)[0:50]
