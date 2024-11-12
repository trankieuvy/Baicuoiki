# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:32:07 2024

@author: Windows
"""
def question_33(nums: list[int]) -> tuple[int, int]:
    if len(nums) < 5:
        return None 
    else:
        nums.sort(reverse = False)
        return nums[-2], nums[4]
        
    
if __name__ == "__main__":
     print(question_33( [3, 1, 4, 5, 9, 2, 6, 8, 7]))
     print(question_33( [1, 3, 2, 5]))