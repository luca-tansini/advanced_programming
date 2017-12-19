import sys

def tail_recursive(func):
    def wrapped(*args):
        #while True:
        try:
            print("\nargs:",*args)
            frame = sys._getframe()
            print(frame)
            print(frame.f_code)
            print(frame.f_back)
            print(frame.f_back.f_code)
            if(frame.f_back.f_back):
                print(frame.f_back.f_back)
                print(frame.f_back.f_back.f_code)
            #Se i due stack frame hanno lo stesso codice sono due record della stessa procedura, quindi sollevo un'eccezione (di tipo TailRecursionException per salvare i parametri) che mi permette di cancellare il record di attivazione corrente
            if(frame.f_back.f_back and frame.f_code == frame.f_back.f_back.f_code):
                print("chiamata ricorsiva! spilo...",end="")
                raise TailRecursionException(*args)
            return func(*args)
        except TailRecursionException as e:
            print("intercettata chiamata ricorsiva con parametri:",*e.args)
            return func(*e.args)
    return wrapped

@tail_recursive
def fact(out,n):
    if(n<3):
        return out
    return fact(out*(n-1),n-1)

class TailRecursionException(Exception):
    def __init__(self,*args):
        self.args=args
