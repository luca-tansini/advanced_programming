#1
def sumMultiples(start, finish, divisors):
    return sum([x for x in range(start,finish+1) if len([n for n in divisors if (x%n == 0)])>0 ])

#2
def leastCommonMultiple(numbers):
    m=max(numbers)
    i=m
    while(True):
        if(len([x for x in numbers if (i%x!=0)]) == 0):
            return i
        else:
            i+=m

#2 Trovato su Internet
from functools import reduce

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(numbers):
    """Return lcm of args."""
    return reduce(lcm, numbers)

#3
def sumFigures(n):
    return sum([int(f) for f in str(n)])


#4
from math import log
import time

def timer(f,*args):
    start = time.time()
    f(*args)
    end = time.time()
    return (end - start)

def fib(n):
    a=1;
    b=1;
    if n<2:
        return b;
    for i in range(2,n):
        b=a+b
        a=b-a
    return b

def findFibWithLen(l):
    i=0;
    while(True):
        if(len(str(fib(i)))>=l):
            return fib(i),i
        i+=1

def findFibWithLenLog(l):
    i=0;
    while(True):
        if(log(fib(i),10)>=l-1):
            return fib(i),i
        i+=1
