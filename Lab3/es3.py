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


class PolishCalculator:

    def __init__(self):
        self.operators = {'+':lambda x,y: x+y,'-':lambda x,y: x-y,'*':lambda x,y: x*y,'/':lambda x,y: x/y,'**':lambda x,y: x**y,'//': lambda x,y: x//y}

    def isoperator(self,x):
        if (x in self.operators): return True
        else : return False

    def eval(self,string):
        l = string.split()
        stack = Stack([])
        for t in l:
            if self.isoperator(t):
                b = float(stack.pop())
                a = float(stack.pop())
                stack.push(self.operators[t](a,b))
            else:
                stack.push(t)
        return stack.pop()

    def str(self,string):
        l = string.split()
        stack = Stack([])
        for t in l:
            if self.isoperator(t):
                b = stack.pop()
                a = stack.pop()
                stack.push("("+a+t+b+")")
            else:
                stack.push(t)
        return stack.pop()
