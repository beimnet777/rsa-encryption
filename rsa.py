from random import *
from math import *

 #creating function for generating random prime numbers
def prime_generator():
 
    x = randint(0, 40)
    y = (x**2) + x + 41
    
    return y

#creating function for generating random prime numbers
def prime_genrator2():
  
    x = randint(0, 27)
    y = 224584605939537911 + 18135696597948930 * x
    return y
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

def e_generating(n2):
    x = randint(2, 150)
    for i in range(n2 - x, 1, -1):
        GCD, Z, L = egcd(i, n2)
        if GCD == 1:
            return i
    return n2 - 1


def encoding(str1, e, n):
    st = ''
    for i in str1:
        st += str(ord(i))
    num = int(st)
 
    result = 1      
    while e > 0:
        if (e%2 == 1):
            result = (result * num)%n
        e = e >> 1
        num = (num * num)% n
    return result



def decode(m, d, n):
    result = 1 
    while d > 0:
        if (d%2 == 1):
            result = (result * m)%n
        d = d >> 1
        m = (m * m)% n
    return result