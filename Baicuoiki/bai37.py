# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:45:37 2024

@author: Windows
"""

def question_36(nums: list[int]) -> list[list[int]]:
    ds = []
    for i in nums: 
        if i == '(':
            ds.append(')')
        elif i == '[':
            ds.append(']')
        elif i == '{':
            ds.append('}')
        elif not ds or ds.pop() != i:
            return False
    return True
if __name__ == "__main__":
    print(question_36( "()"))
    print(question_36( "([)]"))
    
    

