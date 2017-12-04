##!/usr/bin/env python3

import datetime

invkeys = {'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9',' ':' '}

dictionary={
    'w':[],
    '2':{}, # 2:abc
    '3':{}, # 3:def
    '4':{}, # 4:ghi
    '5':{}, # 5:jkl
    '6':{}, # 6:mno
    '7':{}, # 7:pqrs
    '8':{}, # 8:tuvw
    '9':{}, # 9:xyz
}

def builddict(file):
    for line in open(file):
        for word in line.split():
            d=dictionary
            for l in word:
                d.update({strtot9(l):d.get(strtot9(l),{})})
                d=d[strtot9(l)]
            d.update({'w':d.get('w',[])+[word]})
    return dictionary

def strtot9(word):
    out = ""
    for i in range(len(word)):
        out += invkeys[word[i]]
    return out

class t9translator:
    def __init__(self,dictfile):
        self.dict = builddict(dictfile)

    def find(self,num,dict):
        if not num:
            return dict.get('w',[])
        else:
            return self.find(num[1:],dict.get(num[0],{}))

    def rectranslatetext(self,words,index):
        if(index == len(words)-1):
            for s in self.find(words[index],self.dict):
                yield s
        else:
            for s in self.find(words[index],self.dict):
                for s2 in self.rectranslatetext(words,index+1):
                    yield s+" "+s2

    def translatetext(self,text):
        words = list(text.split())
        return [s for s in self.rectranslatetext(words,0)]

#*********************MAIN*************************
if __name__ == "__main__":

    init=datetime.datetime.now()

    t = t9translator("dizionario.txt")

    build=datetime.datetime.now()

    with open('test.txt','r') as f:
        for line in f:
            print(line)
            print(*t.translatetext(line),sep='\n',end='\n...\n')

    translate=datetime.datetime.now()

    print(build-init,translate-build,translate-init)
