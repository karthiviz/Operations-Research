# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:08:16 2022

@author: karthi.vignes
"""

import numpy as np
import math

C_b = np.array([1,3,0])
C_n = np.array([0,0])
A_b = np.array([[-1,1,1],
       [-1,2,0],
       [3,1,0]])
A_n = np.array([[0,0],
       [1,0],
       [0,1]])
b = np.array([3,8,18])

red_costs = C_b.T@np.linalg.inv(A_b)@A_n - C_n.T
obj_value = C_b.T@np.linalg.inv(A_b)@b