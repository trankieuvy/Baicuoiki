# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:54:25 2024

@author: Windows
"""
import random
#12
def question_12():
    n = random.randint(1,100)
    if n < 2:
        return "{} không phải là số nguyên tố".format(n)
    for i in range(2,n):
        if n % i ==0:
            return "{} không phải là số nguyên tố".format(n)
    return "{}  là số nguyên tố".format(n)
if __name__ == "__main__":
     print(question_12())
    #
def question_23(nums: list[int]) -> bool:
    for i in range(len(nums)):
        if nums.count(nums[i])>1:
            return True
    return False
if __name__=="__main__":
    print(question_23([1,2,3,4,5,5,5,5,2,1,1,1,3]))
    print(question_23([1,2,3,4,5]))
