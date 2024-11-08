# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:39:39 2024

@author: Windows
"""

def question_25(nums: list[int]) -> list[int]:
    ds = []
    for i in range(len(nums)):
        ds.append(nums[i] **2) #tạo ra 1 ds mới 
    return sorted(ds, reverse = False)

if __name__ == "__main__":
    print( question_25([-4,-1,0,3,10])) 