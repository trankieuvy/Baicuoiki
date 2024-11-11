# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:54:25 2024

@author: Windows
"""
#11
def question_11(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    sotrc = 0
    sosau = 1
    
    for i in range(2,n+1):
        sohientai = sotrc + sosau
        sotrc=sosau
        sosau=sohientai
    return sohientai
if __name__=="__main__":
    print(question_11(5))
    print(question_11(10))


import random
#12
def question_12():
    n = random.randint(1,100)
    if n < 2:
        return "{} không phải là số nguyên tố".format(n)
    for i in range(2,n):
        if n % i ==0:
            return "{} không phải là số nguyên tố".format(n)
    return "{}  là số nguyên tố".format(n)
if __name__ == "__main__":
     print(question_12())
