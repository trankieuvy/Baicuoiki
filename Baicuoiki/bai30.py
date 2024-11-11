# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:25:23 2024

@author: Windows
"""

def question_30(paragraph: str) -> dict[str, int]:
    tach_tu = paragraph.split()
    tu_dien = {i: tach_tu.count(i) for i in tach_tu}
    return tu_dien
if __name__ == "__main__":
     print(question_30("hello world hello"))
     print(question_30( "apple orange apple banana orange"))
    