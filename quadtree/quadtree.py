from math import sqrt

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

def toQuads(m):
    n = int(sqrt(len(m)))
    l=[]
    ret = [[],[],[],[]]
    for i in range(int(sqrt(len(m)))):
        l+=[(m[i*(int(sqrt(len(m)))):i*(int(sqrt(len(m))))+int(sqrt(len(m)))])]
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

class quadtree:
    def __init__(self,img):
        self.tree = buildTree(toQuads(img))
        self.size = len(img)

    def treerepr(self):
        return repr(self.tree)

    def getimage(self):
        flatquads = self.intgetimage(self.tree,self.size//4)
        rows = toQuads(flatquads)
        img = []
        for r in rows:
            img += r
        return img

    def intgetimage(self,quad,quadsize):
        out = []
        for q in quad:
            if(q == "White"):
                out += [0]*quadsize
            elif(q == "Black"):
                out += [1]*quadsize
            else:
                out += self.intgetimage(q,quadsize//4)
        #print("DEBUG:\n",out)
        return out


import random
size = 64
f = True
count = 0
while(f and count < 10000):
    img = []
    for i in range(size): img+=[random.choice([0,1])]
    q = quadtree(img)
    f = img==q.getimage()
    count+=1

if(not f):
    print("*"*87)
    print("count:",count)
    print("\nimg:")
    print(img)

    print("\nimg matrix repr:")
    m = []
    for i in range(int(sqrt(len(img)))):
        m+=[(img[i*(int(sqrt(len(img)))):i*(int(sqrt(len(img))))+int(sqrt(len(img)))])]
    for r in m: print(r)

    q = quadtree(img)
    print("\ntreerepr:")
    for i in q.tree: print(i)
    print("\nimg == q.getimage() ?",img==q.getimage())
    print("\ngetimage:")
    print(q.getimage())
    print("\nintgetimage:")
    print(q.intgetimage(q.tree,q.size//4))
    print("*"*87)
