##!/usr/bin/env python3

import datetime

invkeys = {'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9',' ':' '}

keys = {'7':['p', 'q', 'r', 's'],'3':['d', 'e', 'f'],'5':['j', 'k', 'l'],'9':['w', 'x', 'y', 'z'],'2':['a', 'b', 'c'],'8':['t', 'u', 'v'],'4':['g', 'h', 'i'],'6':['m', 'n', 'o']}

def builddict(file,prefixsize):
    '''Funzione che preso un file crea il dizionario corrispondente a $file con l'approccio del prof usando parole di $prefixsize caratteri come chiavi'''
    dizionario = dict()
    for line in open(file):
        for word in line.split():
            k = word[:prefixsize]
            dizionario[k] = dizionario.get(k,[]) + [word]
    return dizionario

def strtot9(word):
    '''Funzione che presa una stringa di lettere lowercase e spazi la traduce in una stringa di tasti t9'''
    out = ""
    for i in range(len(word)):
        out += invkeys[word[i]]
    return out

def t9todictkey(t9seq,prefixsize):
    '''Funzione che presa una sequenza di tasti t9 e una lunghezza del prefisso usato nel dizionario restituisce una chiave per il dizionario'''
    if(prefixsize==1 or len(t9seq)==1):
        for c in keys.get(t9seq[0],[]): yield c
    else:
        for c in keys.get(t9seq[0],[]):
            for c2 in t9todictkey(t9seq[1:],prefixsize-1):
                yield c+c2

class t9translator:
    def __init__(self,dictfile,prefixsize):
        self.prefixsize=prefixsize
        self.dict = builddict(dictfile,prefixsize)

    def translateword(self,t9word):
        out = []
        for w in t9todictkey(t9word,self.prefixsize):
            out += [e for e in self.dict.get(w,[]) if strtot9(e)==t9word]
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
