# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:44:57 2024

@author: Windows
"""
import random
def question_17(n: int) -> list:
    ds = [random.randint(1,100) for i in range(n)]
    return sorted(ds, reverse = True)

if __name__ == "__main__":
    print(question_17(8))
