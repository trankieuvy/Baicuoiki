# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:23:45 2024

@author: Windows
"""

def question_21(nums: list[int], target: int) -> tuple[int, int]:
    for i in range(len(nums)): #start = 0, len là có bnhieu số trong chuỗi
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
    return None
if __name__ == "__main__":
    print( question_21([1,2,3,4,5],4))
          
#chạy lần lồng i 1 i[0] = 1,  j[1] = 2 => 1+2 khác 4
        #chạy vòng lặp lòng j i[0] = 1, j[2]=3 => 1+3 = 4
# chạy lồng i i[1] phải chạy hết cái vòng lặp j[1],j[2],.....


