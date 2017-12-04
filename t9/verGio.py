#!/usr/bin/env python3
import datetime

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

def charToN(char):
    if char in 'abc' : return '2'
    if char in 'def' : return '3'
    if char in 'ghi' : return '4'
    if char in 'jkl' : return '5'
    if char in 'mno' : return '6'
    if char in 'pqrs' : return '7'
    if char in 'tuv' : return '8'
    if char in 'wxyz' : return '9'
    return '1'

def find(num,dict=dictionary):
    if not num:
        return dict.get('w',[])
    else:
        return find(num[1:],dict.get(num[0],{}))

def finditer(*phrase):
    if len(phrase)==1:
        return find(phrase[0])
    else:
        return [a+" "+b
            for a in find(phrase[0])
            for b in finditer(*phrase[1:])]

init=datetime.datetime.now()

with open('dizionario.txt','r') as f:
    for word in f:
        word=word.replace("\n","")
        d=dictionary
        for l in word:
            d.update({charToN(l):d.get(charToN(l),{})})
            d=d[charToN(l)]
        d.update({'w':d.get('w',[])+[word]})

build=datetime.datetime.now()

with open('test.txt','r') as f:
    for line in f:
        print(line)
        print(*finditer(*line.strip().split(" ")),sep='\n',end='\n...\n')

translate=datetime.datetime.now()

print(build-init,translate-build,translate-init)
