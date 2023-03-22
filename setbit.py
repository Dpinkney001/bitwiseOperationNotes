# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:25:35 2023

@author: Duvall Pinkney

bitwise operational notes
"""
import math 
import os

def set_bit(x, position):
       mask = 1 << position
       return x | mask
       
def clear_bit(x, position):
    mask = 1 << position
    return x & ~mask

def flip_bit(x,position):
    mask = 1 << position
    return x ^ mask

def is_bit_set(x,position):
    shifted = x >> position
    return shifted & 1

def modify_bit(x, position, state):
    mask = 1 << position
    return (x & ~mask) | (-state & mask)




def operation():
    
    int x = 0
    int position = 0
    int mask = 0
    
    
    x = 01100110
    position = 00000010
    mask = 00000100
    
    int output1
    int output2
    int output3
    int output4
    int output5

    
    print(x)
    print(position)
    print (mask)
    
    
    set_bit(x, position)
    clear_bit(x, position)
    flip_bit(x, position)
    is_bit_set(x, position)
    modify_bit(x, position, state)
    
    
    output1 = set_bit(x, position)
    output2 = clear_bit(x, position)
    output3 = flip_bit(x, position)
    output4 = is_bit_set(x, position)
    output5 = modify_bit(x, position, state)
    
    print(output1)
    print(output2)
    print(output3)
    print(output4)
    print(output5)
   
def main():
    operation()    
    

main()