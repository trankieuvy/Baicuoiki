# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:13:46 2024

@author: Windows
"""

#3
def question_3(s): 
    hoa = 0
    thuong = 0
    for i in s:
        if i.isupper():
            hoa += 1
        if i.islower():
            thuong += 1
    return hoa,thuong
    
if __name__ == "__main__":
    print(question_3("Tran Kieu Vy"))