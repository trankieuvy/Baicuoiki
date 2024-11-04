# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:35:52 2024

@author: Windows
"""
#6
def question_6(n):
    if n <= 0:
        return False 
    tong = 1
    for i in range(1, n+1):
        tong *= i
    return tong
if __name__ == "__main__":
    print(question_6(4))