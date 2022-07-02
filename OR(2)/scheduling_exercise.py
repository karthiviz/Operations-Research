# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:20:20 2022

@author: karthi.vignes
"""

import pandas as pd
import numpy as np
MACHINES = 3

jobs = pd.read_excel('exercise.xlsx', 'Jobs', index_col=0)
jobs.sort_values(by='Processing time', axis=0, ascending=False, inplace=True)
jobs.reset_index(inplace=True)
jobs.index = np.arange(1,len(jobs)+1)
machines = dict(zip(["m"+str(i) for i in range(MACHINES)], [[0,i] for i in range(MACHINES)]))

for i in jobs.index:
    machines = dict(sorted(machines.items(), key=lambda machine: (machine[1][0], machine[1][1])))
    machines[list(machines.keys())[0]][0]+=jobs.loc[i][1]

print(machines)
