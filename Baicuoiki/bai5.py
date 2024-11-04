# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:28:37 2024

@author: Windows
"""
#5
def question_5(lst, x):
    if x in lst: 
        return lst.index(x)
    return None 
if __name__ == "__main__":
    lst = [1,2,3,4,5]
    print(question_5(lst,6))