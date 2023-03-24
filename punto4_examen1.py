# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:28:29 2023

@author: Nicolás Rincón Sánchez
"""

# Taken from the exam explicitly
def funRecursiva(n):
    """
    funRecursiva: Funcion recursiva de parcial 1 
    Creada por Rubén Francisco Manrique Piramanrique
    
    n: nat
    """

    assert (isinstance(n,int)), "Solo se aceptan numeros enteros"
    assert (n>=0), "Solo se aceptan numeros enteros positivos"

    if n==0:
        return 0
    elif n==1:
        return 2
    elif n==2:
        return 68
    
    return 128*funRecursiva(n-3)-32*funRecursiva(n-2)-14*funRecursiva(n-1)


# Function created to evaluate with the solution to the recurrence
def solucionRecursiva(n:int)->int:
    """
    Parameters
    ----------
    n : int
        A number given in order to evaluate the n-th element of a recursion.

    Returns
    -------
    int
        The n-th element in a sequence defined by a recurrence relation.

    """
    c1 = 1
    c2 = -1
    c3 = 1
    eq = c1*2**n + c2*(-8)**n + c3*n*(-8)**n
    return eq

