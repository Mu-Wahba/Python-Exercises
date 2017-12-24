def bin_add(*args):
     return bin(sum(int(x,2) for x in args))[2:]
