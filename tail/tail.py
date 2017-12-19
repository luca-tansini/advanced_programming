import sys,datetime

class TailRecursionException(Exception):
    def __init__(self,*args):
        self.args=args

#DECORATORE PER LA TAIL RECURSION
def tailrecursive(func):
    def wrapped(*args):
        frame = sys._getframe()
        if(frame.f_back.f_back and frame.f_code == frame.f_back.f_back.f_code):
            #intercettata chiamata ricorsiva...
            raise TailRecursionException(*args)
        while True:
            try:
                return func(*args)
            except TailRecursionException as e:
                args=e.args
    return wrapped


def fact(out,n):
    if(n<3):
        return out
    return fact(out*(n-1),n-1)

@tailrecursive
def tfact(out,n):
    if(n<3):
        return out
    return tfact(out*(n-1),n-1)

def fib(i,a,b):
    if(i==0): return a
    return fib(i-1,b,a+b)

@tailrecursive
def tfib(i,a,b):
    if(i==0): return a
    return tfib(i-1,b,a+b)

if __name__ == '__main__':
    print("fib(5000,1,1):")
    try:
        fib(5000,1,1)
    except Exception as e:
        print(e)
    print("\ntfib(5000,1,1):")
    print(tfib(5000,1,1))

    print("\nfact(5000,5000):")
    try:
        fact(5000,5000)
    except Exception as e:
        print(e)
    print("\ntfact(5000,5000):")
    print(str(tfact(5000,5000))[:1000]+"...")

    print("\n\nTimes:")
    
    sys.setrecursionlimit(20000)
    startfib=datetime.datetime.now()
    fib(10000,1,1)
    endfib=datetime.datetime.now()
    tfib(10000,1,1)
    endtfib=datetime.datetime.now()
    print("Tempi fib e tfib:",endfib-startfib,endtfib-endfib)

    startfact=datetime.datetime.now()
    fact(10000,10000)
    endfact=datetime.datetime.now()
    tfact(10000,10000)
    endtfact=datetime.datetime.now()
    print("Tempi fact e tfact:",endfact-startfact,endtfact-endfact)
