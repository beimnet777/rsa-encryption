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