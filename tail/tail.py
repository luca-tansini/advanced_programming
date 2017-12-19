import sys

class TailRecursionException(Exception):
    def __init__(self,*args):
        self.args=args

#DECORATORE PER LA TAIL RECURSION
def tail_recursive(func):
    def wrapped(*args):
        frame = sys._getframe()
        if(frame.f_back.f_back and frame.f_code == frame.f_back.f_back.f_code):
            #intercettata chiamata ricorsiva...
            raise TailRecursionException(*args)
        return func(*args)
    return wrapped

#FUNZIONE TRAMPOLINO PER CHIAMARE LE FUZIONI DECORATE
def tail(func,*args):
    while True:
        try:
            return func(*args)
        except TailRecursionException as e:
            args=e.args

def fact(out,n):
    if(n<3):
        return out
    return fact(out*(n-1),n-1)

@tail_recursive
def trfact(out,n):
    if(n<3):
        return out
    return trfact(out*(n-1),n-1)

def fib(i,a,b):
    if(i==0): return a
    return fib(i-1,b,a+b)

@tail_recursive
def trfib(i,a,b):
    if(i==0): return a
    return trfib(i-1,b,a+b)

if __name__ == '__main__':
    print("fib(5000,1,1):")
    try:
        fib(5000,1,1)
    except Exception as e:
        print(e)
    print("\ntail(trfib,5000,1,1):")
    print(tail(trfib,5000,1,1))

    print("\nfact(5000,5000):")
    try:
        fact(5000,5000)
    except Exception as e:
        print(e)
    print("\ntail(trfact,5000,5000):")
    print(str(tail(trfact,5000,5000))[:1000]+"...")
