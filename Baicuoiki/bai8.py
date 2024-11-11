# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:51:04 2024

@author: Windows
"""

def question_8() -> str:
    nhap = input("Nhập vào bàn phím: ")
    return nhap[::-1] 
 
if __name__ == "__main__":
    print(question_8())
