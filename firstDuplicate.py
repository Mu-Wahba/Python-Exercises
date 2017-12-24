#first duplicate if no duplications result will be -1

def firstDuplicate(a):
    D={i:a.count(i) for i in a}
    for k,v in D.items():
        if v > 1:
            return(k)
    else:
        return(-1)
