#keep the first ocuuerence of a word and remove the other

def Keep1stOcc(s,w):
     i=s.find(w)+len(w)
     return s[:i]+s[i:].replace(w+' ','')





def Keep1stOcc(s,w):
    TUP=s.partition(w)
    return TUP[0]+TUP[1]+TUP[2].replace(w+" ",'')
