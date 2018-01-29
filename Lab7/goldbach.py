def isprime(n):
    i = 2
    while(i**2 <= n):
        if(n%i==0): return False
        i+=1
    return True

def primegenerator(n,m):
    for x in range(n,m):
        if(isprime(x)): yield x

def goldbach(n):
    if(n <= 2 or n%2): raise ValueError("Arguments must be even!")
    c = n//2
    for i in primegenerator(c,n):
        if(isprime(n-i)): return (n-i,i)
    return "Goldbach fails!"

def goldbach_list(n,m):
    if(n%2): n = n+1
    d = dict()
    for i in range(n,m,2):
        d[i] = goldbach(i)
    return d
