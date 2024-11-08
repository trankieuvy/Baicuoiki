# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:22:46 2024

@author: Windows
"""

def question_24(nums: list[int]) -> int:
    return max(nums, key = nums.count)

if __name__ == "__main__":
    print( question_24([1,1,2,3,4,4,5]))      
    
