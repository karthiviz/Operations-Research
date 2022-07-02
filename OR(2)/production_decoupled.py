# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:15:21 2022

@author: karthi.vignes
"""

from gurobipy import *

#indices
products = range(2)
resources = range(3)

#objective function coefficients
prices = [700, 900]

#constraint coefficients and upper bounds
resource_consum = [[3, 5],
                   [1, 2],
                   [50, 20]]
resource_avail = [3600, 1600, 48000]


m_dec = Model('m_dec')
x = [m_dec.addVar(lb=0, vtype = GRB.CONTINUOUS, name = 'x'+str(i)) for i in products]
m_dec.setObjective(quicksum(x[i] * prices[i] for i in products), GRB.MAXIMIZE)
m_dec.addConstrs((quicksum(resource_consum[j][i] * x[i] for i in products) <= resource_avail[j] for j in resources), 'Resource_Caps')
m_dec.optimize()