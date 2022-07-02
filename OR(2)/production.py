# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:01:08 2022

@author: karthi.vignes
"""

from gurobipy import *

m = Model('m')

x1 = m.addVar(lb=0, vtype = GRB.CONTINUOUS, name = 'x1')
x2 = m.addVar(lb=0, vtype = GRB.CONTINUOUS, name = 'x2')

m.setObjective(700 * x1 + 900 * x2, GRB.MAXIMIZE)
m.addConstr(3 * x1 + 5 * x2 <= 3600, 'resource_wood')
m.addConstr(x1 + 2 * x2 <= 1600, 'resource_labour')
m.addConstr(50 * x1 + 20 * x2 <= 48000, 'resource_labour')

m.optimize()
