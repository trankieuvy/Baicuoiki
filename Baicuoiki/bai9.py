# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:03:19 2024

@author: Windows
"""
def question_9(s: str) -> bool:
    s = s.lower()
    chuoi = [i for i in s if i.isalnum()]
    return chuoi == chuoi[::-1]
 
if __name__ == "__main__":
     print(question_9("madam"))
     print(question_9("race a car"))
     print(question_9("A man, a plan, a canal: Panama"))
    
