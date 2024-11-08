# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:44:57 2024

@author: Windows
"""
import random
def question_17(n: int) -> list:
    ds = []
    for i in range(n):
        so = random.randint(1,100)
        ds.append(so)
    return sorted(ds, reverse= False)

if __name__ == "__main__":
    print(question_17(8))