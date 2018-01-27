import traceback,sys

def memoization(method):
    def wrapper(self,*args):
        #se non ho ancora una tabella la crea
        try:
            self.memoizationtable
        except Exception as e:
            self.memoizationtable = dict()
        #se non ho ancora una entry per il metodo nella tabella la crea
        try:
            self.memoizationtable[method.__name__]
        except Exception as e:
            self.memoizationtable[method.__name__] = dict()

        if(self.memoizationtable[method.__name__].get(args)):
            print("got it! -- "+method.__name__+str(args)+" = "+str(self.memoizationtable[method.__name__][args]))
            return self.memoizationtable[method.__name__][args]
        else:
            print("calculating "+method.__name__+str(args)+" for the first time")
            self.memoizationtable[method.__name__][args] = method(self,*args)
            return self.memoizationtable[method.__name__][args]
    return wrapper

def stack_trace(method):
    def wrapper(*args):
        print('-'*((60-len((method.__name__+str(args[1:]))))//2),end="")
        print(method.__name__+str(args[1:]),end="")
        print('-'*((61-len((method.__name__+str(args[1:]))))//2))
        traceback.print_stack(f=sys._getframe().f_back)
        print("-"*60)
        return method(*args)
    return wrapper

class MyMathWithMemo:

    @memoization
    def fib(self,n):
        if(n < 0):
            raise ValueError("fib not defined for negative values")
        if(n < 2):
            return 1
        return self.fib(n-2) + self.fib(n-1)

    @memoization
    def fact(self,n):
        if(n < 0):
            raise ValueError("fact not defined for negative values")
        if(n <= 2):
            return n
        return n * self.fact(n-1)

class MyMathWithStack:

    @stack_trace
    def fib(self,n):
        if(n < 0):
            raise ValueError("fib not defined for negative values")
        if(n < 2):
            return 1
        return self.fib(n-2) + self.fib(n-1)

    @stack_trace
    def fact(self,n):
        if(n < 0):
            raise ValueError("fact not defined for negative values")
        if(n <= 2):
            return n
        return n * self.fact(n-1)
