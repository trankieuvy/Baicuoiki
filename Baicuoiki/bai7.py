# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:41:35 2024

@author: Windows
"""
import random 
#7
def question_7(n):
    lon = 0
    nho = 1
    for i in range(n):        
        so = random.uniform(0,1)
        print("Số ngẫu nhiên: ",so)
        lon = max(lon,so)
        nho = min(nho,so)
    return lon,nho
if __name__ == "__main__":
    print(question_7(4))