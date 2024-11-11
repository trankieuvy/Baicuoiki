# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:36:29 2024

@author: Windows
"""

def question_28(s: str) :
    #cach1
    dem = {i: s.count(i) for i in s }
    #cach 2
    dict_name = {}
    for i in s:
       if i in dict_name:
           dict_name[i] += 1
       else:
           dict_name[i] = 1
    
    return dict_name, dem

if __name__ == "__main__":
    print(question_28("Hello"))
    print(question_28("test"))