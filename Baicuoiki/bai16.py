# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:28:58 2024

@author: Windows
"""
import math 
def question_16(*args) -> float:
    if len(args) == 0:
        return None
    else:
        tong = sum(args)
        tbc = tong / len(args)
        return  tbc
if __name__ == "__main__":
    print(question_16())
    print(question_16(0))
    