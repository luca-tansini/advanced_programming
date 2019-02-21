'''
Write a decorator which wraps functions to log function arguments and the return value on each call.
Provide support for both positional and named arguments (your wrapper function should take both
*args and **kwargs and print them both)
'''

def logged(func):
    def wrapped(*args,**kargs):
        out = 'you called: '+func.__name__+'('
        out+= ','.join([str(a) for a in args])
        if(kargs):
            for k,v in kargs.items():
                out+=','+k+'='+str(v)
        out+=')'
        print(out)
        ret = func(*args,**kargs)
        print('it returned: '+str(ret))
        return ret
    return wrapped

@logged
def pippo(a,b,molt=1):
    return (a+b)*molt

pippo(2,3)
pippo(2,3,molt=6)

@logged
def func(*args):
    return 3 + len(args)

func(4,4,4)
