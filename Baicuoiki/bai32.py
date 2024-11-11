# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:35:41 2024

@author: Windows
"""
def question_32(nums: list[int]) -> tuple[list[int], list[int]]:
    chan = sorted( [i for i in nums if i %2 == 0], reverse = True)
    le = sorted([ i for i in nums if i % 2 != 0])
    return chan, le
if __name__ == "__main__":
    print(question_32([4, 1, 3, 2, 7, 8, 5]))
    print(question_32( [9, 12, 15, 6, 2, 14]))
    