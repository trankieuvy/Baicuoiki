# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:00:00 2024

@author: Windows
"""
import random 
#2
def question_2(n):
    tong = 0
    for i in range(n):
        so = random.randint(1,100)
        print("Số ngẫu nhiên: ",so)
        tong += so 
    tb = tong / n
    return tong, tb    
    
if __name__ == "__main__":
    print(question_2(4))