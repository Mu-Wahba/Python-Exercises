##def fab(n):
##     a,b=0,1
##     for _ in range(n):
##          a,b=b,a+b
##     return(a)


def fab2(n):
     if n <=1: return n
     return fab2(n-1)+fab2(n-2)
