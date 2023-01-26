# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:54:10 2022

@author: karthi.vignes
"""

import pandas as pd
from gurobipy import *
AMBULANCES = 3

path = "C:/Users/karthi.vignes/Documents/GitHub/Operations-Research/OR(2)/"
distances = pd.read_excel(path+'final.xlsx', 'Distances')
population = pd.read_excel(path+'final.xlsx', 'Population')

#indices
districts = range(len(distances['District']))
ambulances = range(AMBULANCES)

#data
distance_dict = distances.set_index('District').T.to_dict('list')
population = population['Population']

ambulance = Model('ambulance')

#adding variables, variable constraints
x = [ambulance.addVar(lb=0, vtype=GRB.BINARY, name="x"+str(i+1)) for i in districts]
w = [ambulance.addVar(lb=0, vtype=GRB.INTEGER, name="w"+str(i+1)) for i in districts]
y = [[ambulance.addVar(lb=0, vtype=GRB.BINARY, name="y"+str(i+1)+str(j+1)) for i in districts] for j in districts]
pop_weighted = ambulance.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = "firefighting_times")
ambulance.update()

#objective function
ambulance.setObjective(pop_weighted, GRB.MINIMIZE)

#constraints
ambulance.addConstr(quicksum(x[j] for j in districts) == AMBULANCES)
ambulance.addConstrs(y[i][j] <= x[i] for i in districts for j in districts)
ambulance.addConstrs((quicksum(y[i][j] for i in districts) == 1 for j in districts))
ambulance.addConstrs((quicksum(y[i][j] * distance_dict[i+1][j] for i in districts) <= w[j]) for j in districts)
ambulance.addConstrs((pop_weighted >= w[i] * population[i] for i in districts))
ambulance.update()

ambulance.optimize()

for c in ambulance.getConstrs():
    if c.Slack > 1.0e-6:
        print(c.ConstrName)