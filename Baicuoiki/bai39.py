# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:40:06 2024

@author: Windows
"""
def question_39(prices: list[int]) -> int:
     min_prices = prices[0]
     max_prices = 0
     for i in range(1, len(prices)):
         gia_hien_tai = prices[i]- min_prices
         max_prices = max(max_prices, gia_hien_tai)
         min_prices = min(min_prices, prices[i])
     return max_prices 
if __name__ == "__main__":
    print(question_39([6, 7, 8, 9, 20, 5]))   
    print(question_39([7, 1, 5, 3, 6, 4]))   
    print(question_39([7, 6, 4, 3, 1]))

#Cách 2
def question_39(prices: list[int]) -> int:
    min_prices = 10**9
    max_prices =0
    for i in prices:
        if i < min_prices:
            min_prices = i
        elif i - min_prices> max_prices:
            max_prices = i-min_prices
    return max_prices
if __name__=="__main__":
    print(question_39([6, 7, 8, 9, 20, 5]))
    print(question_39([7, 1, 5, 3, 6, 4]))
    print(question_39([7, 6, 4, 3, 1]))

            
         
          

