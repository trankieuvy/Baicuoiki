# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:44:23 2024

@author: Windows
"""

#10
def question_10() -> None:
    ds = input("Nhập danh sách: ")
    tach = ds.split()
    if tach:
        return ''.join([i for i in tach])
    return None

if __name__ == "__main__":
     print(question_10())
