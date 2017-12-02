from math import sqrt

def deepcount(l):
    count = 0
    for i in l:
        if isinstance(i,list):
            count += deepcount(i)
        else:
            count += 1
    return count

def buildTree(quads):
    for i in range(4):
        c = getQuadColor(quads[i])
        if(c != "Grey"):
            quads[i] = c
        else:
            quads[i] = buildTree(toQuads(quads[i]))
    return quads

def getQuadColor(q):
    c = sum(q)
    if(c == len(q)):
        return "Black"
    elif(c == 0):
        return "White"
    return "Grey"

def torows(l):
    n = int(sqrt(len(l)))
    return [l[i*n:i*n+n] for i in range(n)]

def toQuads(m):
    n = int(sqrt(len(m)))
    l=torows(m)
    ret = [[],[],[],[]]
    for i in range(0,int(n/2)):
        for j in range(0,int(n/2)):
            ret[0]+=[l[i][j]]
    for i in range(0,int(n/2)):
        for j in range(int(n/2),n):
            ret[1]+=[l[i][j]]
    for i in range(int(n/2),n):
        for j in range(0,int(n/2)):
            ret[2]+=[l[i][j]]
    for i in range(int(n/2),n):
        for j in range(int(n/2),n):
            ret[3]+=[l[i][j]]
    return ret

def flatten(l):
    out = []
    for e in l:
        out += e
    return out

class quadtree:

    def __init__(self,img):
        self.tree = buildTree(toQuads(img))
        self.size = len(img)

    def treerepr(self):
        return repr(self.tree)

    def getimage(self):
        sidesize = int(self.size**0.5)
        img = [[0]*sidesize for i in range(sidesize)]
        self.intgetimage(self.tree,sidesize//2,0,0,img)
        return flatten(img)

    def intgetimage(self,quads,quadsize,xstart,ystart,img):
        '''quads è la lista di quadranti, quadsize è la dimensione del lato di un quadrante a questo livello, xstart e ystart sono gli indici di inizio del primo quadrante, img è l'immagine che viene costruita'''

        for q in range(4):
            qxstart = xstart + quadsize * (q%2)
            qystart = ystart + quadsize * (q//2)
            if(isinstance(quads[q],str)):
                for i in range(qystart,qystart+quadsize):
                    for j in range(qxstart,qxstart+quadsize):
                        img[i][j] = 0 if quads[q] == 'White' else 1
            else:
                self.intgetimage(quads[q],quadsize//2,qxstart,qystart,img)

    def calculatesavedspace(self):
        print("original size: ",self.size)
        print("compressed size: ",deepcount(self.tree))
        print("saved space: ",self.size - deepcount(self.tree))
        return self.size - deepcount(self.tree)

import random

def testsave(size):
    img = [random.choice([0,1]) for i in range(size)]
    q = quadtree(img)
    return q.calculatesavedspace()


def test(size,reps=1000):
    f = True
    count = 0

    while(f and count < reps):
        img = [random.choice([0,1]) for i in range(size)]
        q = quadtree(img)
        f = img==q.getimage()
        count+=1

    if(not f):
        print("*"*87)
        print("count:",count)
        print("\nimg:")
        print(img)

        print("\nimg matrix repr:")
        for r in torows(img): print(r)

        q = quadtree(img)
        print("\ntreerepr:")
        for i in q.tree: print(i)
        print("\ngetimage:")
        img = q.getimage()
        print(quadtree.torows(img))
        print("*"*87)
    else:
        print("TEST OK")
