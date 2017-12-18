class Node:
    def __init__(self,v,l,r):
        self.value = v
        self.left = l
        self.right = r

def visit(tree,dict):
    if(tree.value in ['+','-','*','/']):
        return dict[tree.value](visit(tree.left,dict),visit(tree.right,dict))
    return dict[tree.value]

class calculator:
    def __init__(self,input):
        self.input = input
        n, self.ast = self.buildtree(0)

    def buildtree(self,i):
        if(self.input[i] in ['+','-','*','/']):
            j,l = self.buildtree(i+1)
            j,r = self.buildtree(j)
            return j,Node(self.input[i],l,r)
        return i+1,Node(self.input[i],None,None)

    codedict = dict({\
    ('+', lambda x,y:x+"\n"+y+"\n"+"add"),\
    ('-', lambda x,y:x+"\n"+y+"\n"+"sub"),\
    ('*', lambda x,y:x+"\n"+y+"\n"+"mul"),\
    ('/', lambda x,y:x+"\n"+y+"\n"+"div")})
    codedict.update({(str(n),"store " + str(n)) for n in range(10)})

    def code(self):
        return visit(self.ast,self.codedict)

    evaldict = dict({\
    ('+', lambda x,y:int(x)+int(y)),\
    ('-', lambda x,y:int(x)-int(y)),\
    ('*', lambda x,y:int(x)*int(y)),\
    ('/', lambda x,y:int(x)/int(y))})
    evaldict.update({(str(n),n) for n in range(10)})

    def eval(self):
        return visit(self.ast,self.evaldict)
