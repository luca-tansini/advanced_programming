class Stack:
    def __init__(self,alist):
        self.stack = alist

    def __len__(self):
        return len(self.stack)

    def pop(self):
        tmp = self.stack[0]
        self.stack = self.stack[1:]
        return tmp

    def push(self,x):
        self.stack = [x]+self.stack

operators = {'+':lambda x,y: x+y,'-':lambda x,y: x-y,'*':lambda x,y: x*y,'/':lambda x,y: x/y}

def isoperator(x):
    operators = ["+","-","*","/"]
    if (x in operators): return True
    else : return False

def eval(string):
    l = string.split()
    stack = Stack([])
    for t in l:
        if isoperator(t):
            b = float(stack.pop())
            a = float(stack.pop())
            stack.push(operators[t](a,b))
        else:
            stack.push(t)
    return stack.pop()
