def factGenerator():
    i=1
    n=1
    while True:
        yield n
        n*=(i+1)*(i+2)
        i=i+2

def taylorSin(x,n):
    gen = factGenerator()
    return sum([ ((-1)**i)*(x**(2*i+1))/next(gen) for i in range(n)])
