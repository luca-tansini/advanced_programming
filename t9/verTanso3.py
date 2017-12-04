##!/usr/bin/env python3

import datetime

invkeys = {'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9',' ':' '}

def builddict(file,prefixsize):
    dizionario = dict()
    for line in open(file):
        for word in line.split():
            k = word[:prefixsize]
            lvl1 = dizionario.get(strtot9(k),0)
            if(lvl1):
                lvl2 = lvl1.get(len(word),0)
                if(lvl2):
                    lvl2 += [word]
                else:
                    lvl1.update({len(word):[word]})
            else:
                dizionario[strtot9(k)] = {len(word):[word]}
    return dizionario

def strtot9(word):
    out = ""
    for i in range(len(word)):
        out += invkeys[word[i]]
    return out

class t9translator:
    def __init__(self,dictfile,prefixsize):
        self.prefixsize=prefixsize
        self.dict = builddict(dictfile,prefixsize)

    def translateword(self,t9word):
        out = [e for e in self.dict.get(t9word[:self.prefixsize],dict()).get(len(t9word),[]) if strtot9(e)==t9word]
        return out

    def rectranslatetext(self,words,index):
        if(index == len(words)-1):
            for s in self.translateword(words[index]):
                yield s
        else:
            for s in self.translateword(words[index]):
                for s2 in self.rectranslatetext(words,index+1):
                    yield s+" "+s2

    def translatetext(self,text):
        words = list(text.split())
        return [s for s in self.rectranslatetext(words,0)]

#*********************MAIN*************************
if __name__ == "__main__":

    init=datetime.datetime.now()

    t = t9translator("dizionario.txt",5)

    build=datetime.datetime.now()

    with open('test.txt','r') as f:
        for line in f:
            print(line)
            print(*t.translatetext(line),sep='\n',end='\n...\n')

    translate=datetime.datetime.now()

    print(build-init,translate-build,translate-init)
