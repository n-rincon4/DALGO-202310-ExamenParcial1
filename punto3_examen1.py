# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:12:03 2023

@author: Nicolás Rincón Sánchez
"""

def parentesisAnidados(cadena:str)->bool:
    """
    This function uses a Python list as a stack

    Parameters
    ----------
    cadena : str
        A string composed of any combination of square, circular or curved
        parentheses (that is "(",")","[","]","{","}").

    Returns
    -------
    bool
        True, if all parentheses are correctly paired and nested "[{()}]()".
        False, otherwise.

    """
    i = 0
    c = ""
    n = len(cadena)
    stack = list() #Python list that will be used as a stack
    
    continuar, correcto = True, True
    if len(cadena)%2 != 0:
        continuar, correcto = False, False
    
    if continuar:
        while i<n:
            if (cadena[i]=="(" or cadena[i]=="[" or cadena[i]=="{"):
                stack.append(cadena[i]) #Implementation of PUSH method
            else:
                c = stack[-1] if stack else None #Implementation of TOP method
                
                if ((cadena[i]==")" and c=="(") or (cadena[i]=="]" and c=="[") 
                    or (cadena[i]=="}" and c=="{")):
                    
                    stack.pop() #Implementation of POP method
                else:
                    continuar, correcto = False, False
            i += 1
    
    if len(stack)!=0:
        correcto = False
        
    return correcto
