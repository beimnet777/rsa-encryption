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
