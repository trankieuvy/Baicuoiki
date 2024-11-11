# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:04:34 2024

@author: Windows
"""
# tìm trung vị


def question_29(nums: list[int]) -> float:
    nums.sort()
    n = len(nums)
    if n % 2 != 0:
        return nums[n//2]
    return (nums[n//2 -1 ] + nums[n //2]) /2
if __name__ == "__main__":
    print(question_29([1, 3, 4, 2, 5]))
    print(question_29([1, 2, 3, 4]))
        
            
    