x=[1,2,4,8]

add=0
for i in x:
     add=add+i
print(add)


import functools
print(functools.reduce(lambda x,y:x+y,x))

import itertools
y=[f for f in list(itertools.accumulate(x))]
print(y[-1])
