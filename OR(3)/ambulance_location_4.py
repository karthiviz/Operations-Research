# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:54:10 2022

@author: karthi.vignes
"""

import pandas as pd
from gurobipy import *
import json
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
callback_count = 0
noderelsol = {}

# Callback - use lazy constraints to record node relaxation solutions
def relaxedsol(model, where):
    global callback_count
    global noderelsol
    with open(path+'noderelsol.json', 'w', encoding='utf-8') as f:
        if where == GRB.callback.MIPNODE:
            if model.cbGet(GRB.callback.MIPNODE_STATUS) == GRB.status.OPTIMAL:
                callback_count+=1
                mvars = model.getVars()
                x = model.cbGetNodeRel(mvars)
                names = model.getAttr('VarName', mvars)
                noderelsol[callback_count] = dict(zip(names,x))
        #json.dump(noderelsol, f, ensure_ascii=False, indent=4)

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
ambulance.addConstr((quicksum(x[j] for j in districts) == AMBULANCES), "All ambulances assigned to districts")
ambulance.addConstrs((y[i][j] <= x[i] for i in districts for j in districts), "Assigned ambulance must be from an Amb dist")
ambulance.addConstrs(((quicksum(y[i][j] for i in districts) == 1 for j in districts)), "Each district assigned Max. 1 Ambulance")
ambulance.addConstrs(((quicksum(y[i][j] * distance_dict[i+1][j] for i in districts) <= w[j]) for j in districts), "Dist from ambulance dist to assigned dist")
ambulance.addConstrs(((pop_weighted >= w[i] * population[i] for i in districts)), "Max time requirements")
ambulance.update()

ambulance._x = x
ambulance.Params.LazyConstraints = 1
ambulance.optimize(relaxedsol)

dvars = ambulance.getVars()
constrs = ambulance.getConstrs()
obj_coeffs = ambulance.getAttr('Obj', dvars)
const_coeffs = ambulance.getA()
print(obj_coeffs)
print(const_coeffs.toarray())
