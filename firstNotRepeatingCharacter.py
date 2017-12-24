def firstNotRepeatingCharacter(s):
    D={i:s.count(i) for i in s}
    for k,v in D.items():
        if v==1:
            return k
    else:
        return('-')
