# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:17:17 2024

@author: Windows
"""

def question_20() ->str:
    nhap = input("Người dùng nhập: ")
    if nhap == "":
        return None 
    return nhap
if __name__ == "__main__":
    print( question_20())