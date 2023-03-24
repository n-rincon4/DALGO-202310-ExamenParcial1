# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:01:16 2023

@author: Nicolás Rincón Sánchez
"""

def kunico(S:list, k:int)->bool:
    """
    Parameters
    ----------
    S : list
        An array of natural numbers.
    k : int
        A positive integer.

    Returns
    -------
    bool
        True, if the array is k-unique: there are no repeated elements in
        positions closer than k units from each other.
        False, otherwise.
        
    """
    i = 0
    continuar, unico = True, True
    if continuar:
        while i<len(S):
            j = 1
            while j<=k and j+i<len(S):
                if S[i] == S[i+j]:
                    continuar, unico = False, False
                j += 1
            i += 1
    return unico
