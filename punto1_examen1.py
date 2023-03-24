# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:12:55 2023

@author: Nicolás Rincón Sánchez
"""

# Recursive implementation
def main(S:list)->bool:
    return subDobleRecursive(S,sum(S)/2,len(S)-1)
    
    
def subDobleRecursive(S:list, R:int, i:int)->bool:
    """
    Parameters
    ----------
    S : list
        An array of natural numbers.
    R : int
        The target sum of the array

    Returns
    -------
    bool
        True, if the array can be split into two subarrays each with equal sum.
        False, otherwise.
        
    """
    if 2*R%2 != 0:
        return False
    if (R<0) or (i==0 and R>0):
        return False
    if R==0:
        return True
    if (i>0 and R>0):
        if S[i]>R:
            return subDobleRecursive(S, R, i-1)
        else:
            return subDobleRecursive(S, R, i-1) or subDobleRecursive(S, R-S[i], i-1)
        
        
# Implementation using Dynamic Programming
def subDobleDP(S:list)->bool:
    """
    This algorithm uses Memoization and Tabulation instead of recursive calls.
    
    Parameters
    ----------
    S : list
        An array of natural numbers.

    Returns
    -------
    bool
        True, if the array can be split into two subarrays each with equal sum.
        False, otherwise.

    """
    n = len(S)
    R = sum(S)
    matriz = [[False for j in range(int(R/2) + 1)] for i in range(len(S)+1)]
    
    existe, continuar = True, True
    if R%2 != 0:
        existe, continuar = False, False
    
    if continuar == True:
        i = n
        while i>=0:
            matriz[i][0] = True
            i -= 1
            
        j = 1
        while j<=int(R/2):
            matriz[0][j] = False
            j += 1
        
        i = 1
        while i<=n:
            j = 1
            while j<=int(R/2):
                if j-S[i-1]<0:
                    matriz[i][j] = matriz[i-1][j]
                else:
                    matriz[i][j] = matriz[i-1][j] or matriz[i-1][j-S[i-1]]
                j += 1
            i += 1
        
        existe = matriz[n][int(R/2)]
    
    print(matriz)
    return existe
