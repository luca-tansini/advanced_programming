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
