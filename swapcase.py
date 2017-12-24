def seap(st):
    st=input()
    for char in st:
        if char.islower()is True :
            return(char.upper(),end='')

        elif char.isupper()is True :
            return(char.lower(),end='')
        else:
            return(char,end='')


