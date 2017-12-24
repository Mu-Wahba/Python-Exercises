import itertools
def grop(string):
     for k,g in itertools.groupby(string):
          return((str(len(list(g)))+k).replace('1',''),end='')
