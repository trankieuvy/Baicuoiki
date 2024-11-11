# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 03:09:01 2024

@author: Windows
"""
import collections

def question_26(s: str) -> int:
    char_count = collections.Counter(s)
    length = 0
    odd_found = False 
    for count in char_count.values():
        length += (count // 2 )* 2
        
        if count % 2 == 1:
            odd_found = True
    if odd_found:
        length += 1

    return length

print(question_26("abccccdd"))