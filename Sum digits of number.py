#Sum the digits of a number 

def sum_digits(num):
     """This is a recursive function
    to find Sum the digits of a number """
     if num == 0 : return 0
     return sum_digits(num // 10)+num%10



def sum_digits2(num):
     return sum(map(int,str(num)))
