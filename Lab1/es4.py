def findMax(m):
    mas = max(m[0])
    for r in m[1:]:
        tmp=max(r)
        mas = tmp if tmp > mas else mas
    return mas

def printMatrix(m):
    l=len(str(findMax(m)))
    for r in m:
        s="|"
        for e in r:
            s+=("{: "+str(l+1)+"d}  ").format(e)
        print(s+"|")

def identity(n):
    return [ [1 if e==i else 0 for e in range(n)] for i in range(n)]

def square(n):
    return [ [e*e for e in range(n*i,n*(i+1))] for i in range(n) ]

def transpose(m):
    return [ [ m[j][i] for j in range(len(m)) ] for i in range(len(m[0])) ]

def multiply(m,p):
    if(len(m[0])!=len(p)):
        raise NameError("Matrici di dimensioni non moltiplicabili tra loro!")
    return [ [ sum([ m[i][k]*p[k][j] for k in range(len(m[0])) ]) for j in range(len(p[0])) ] for i in range(len(m)) ]
