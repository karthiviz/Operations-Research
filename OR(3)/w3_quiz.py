# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:08:16 2022

@author: karthi.vignes
"""

import numpy as np
import math

C_b = np.array([2,3,0])
C_n = np.array([0,0,0])
A_b = np.array([[1,1,0],
       [1,2,0],
       [0,1,1]])
A_n = np.array([[1,1,0],
       [0,0,1],
       [1,0,0]])
b = np.array([4,6,1])

red_costs = C_b.T@np.linalg.inv(A_b)@A_n - C_n.T
obj_value = C_b.T@np.linalg.inv(A_b)@b
A_b_inv_b = np.linalg.inv(A_b)@b
A_b_inv_A_n = np.linalg.inv(A_b)@A_n

print(red_costs)
print(obj_value)
print(A_b_inv_b)
print(A_b_inv_A_n)