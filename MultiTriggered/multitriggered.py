def multi_triggered(n,l):
    def dec(F):
        def wrapped(*args):
            wrapped.count += 1
            print("Chiamata numero "+str(wrapped.count))
            return F(*args)
        wrapped.count = 0
        return wrapped
    return dec

@multi_triggered(1,2)
def func(a,b,c,d):
    print(a+b)
    return
