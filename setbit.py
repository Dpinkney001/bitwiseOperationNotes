# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:25:35 2023

@author: Duvall Pinkney

bitwise operational notes
"""
def main:
        
    int x = 01100110
    int position = 00000010
    int mask = 00000100
    
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
    
    

