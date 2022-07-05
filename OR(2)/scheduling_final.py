# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 13:49:04 2022

@author: karthi.vignes
"""

import pandas as pd
from gurobipy import *
import ast
MACHINES = 3

data = pd.read_excel('final.xlsx', 'Jobs')
data['Conflicting jobs'] = data['Conflicting jobs'].apply(ast.literal_eval)

#indices
jobs = range(len(data['Job']))
machines = range(MACHINES)

#data
conflicting_jobs_dict = dict(zip(data['Job'], data['Conflicting jobs']))
processing_times = dict(zip(data['Job'], data['Processing time']))

makespan = Model('makespan.lp')

#adding variables, variable constraints
x = [[makespan.addVar(lb=0, vtype=GRB.BINARY, name="x"+str(j+1)+str(i+1)) for i in jobs] for j in machines]
w = makespan.addVar(ub=128, vtype=GRB.CONTINUOUS, name="w")
makespan.update()

#objective function
makespan.setObjective(w, GRB.MINIMIZE)

#constraints
makespan.addConstrs(quicksum(x[i][j] for i in machines) == 1 for j in jobs)
makespan.addConstrs(x[i][1]+x[i][4]+x[i][7] <= 1 for i in machines)
makespan.addConstrs(x[i][5]+x[i][8] <= 1 for i in machines)
makespan.addConstrs(x[i][6]+x[i][9] <= 1 for i in machines)
makespan.addConstrs(x[i][10]+x[i][14] <= 1 for i in machines)
makespan.addConstrs((quicksum(x[i][j] * processing_times[j+1] for j in jobs) <= w) for i in machines)
makespan.update()

makespan.optimize()
