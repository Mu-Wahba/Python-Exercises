#Factorial of number by 4 different ways

from functools import reduce
from itertools import accumulate


def fact1(n):
    if n==0:return 1
    return reduce(lambda x,y:x*y , [i for i in range(1,n+1)])    

def fact2(n):
    if n==0:return 1
    return fact2(n-1)*n

def fact3(n):
    if n==0:return 1
    return list(accumulate([i for i in range(1,n+1)],lambda x,y:x*y))[-1]

def fact4(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    return f
        
