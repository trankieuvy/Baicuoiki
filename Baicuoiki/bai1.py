# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:52:43 2024

@author: Windows
"""
#1
def question_1(n):
    if n < 2:
        return False 
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    print(question_1(4))