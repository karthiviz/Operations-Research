# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 13:11:54 2022

@author: karthi.vignes
"""

import pandas as pd
from gurobipy import *

basic = pd.read_excel('week3.xlsx', 'Basic information')
cities = range(len(basic['City']))
markets = range(len(basic['Market']))

city_info = pd.read_excel('week3.xlsx', 'City\'s information')
operating_costs = city_info['Operating cost']
capacity = city_info['Capacity']

market_info = pd.read_excel('week3.xlsx', 'Market\'s information')
demand = market_info['Demand']

shipping_info = pd.read_excel('week3.xlsx', 'Shipping cost', index_col=0)
shipping_costs = [list(shipping_info.loc[i]) for i in shipping_info.index]

facility = Model('facility')

#adding variables, variable constraints
x = [facility.addVar(lb=0, vtype=GRB.BINARY, name="x"+str(j+1)) for j in cities]
y = [[facility.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y"+str(i+1)+str(j+1)) \
      for j in cities] for i in markets]

#setting Objective function
facility.setObjective(quicksum(operating_costs[j]*x[j] for j in cities)\
                      +quicksum(quicksum(shipping_costs[i][j] * y[i][j]\
                                         for j in cities) for i in markets),\
                          GRB.MINIMIZE)

#adding functional constraints
facility.addConstrs((quicksum(y[i][j] for i in markets) <= x[j] * capacity[j] \
                    for j in cities), "Prod Constraints")

facility.addConstrs((quicksum(y[i][j] for j in cities) >= demand[i] for i in\
                     markets), "Demand fulfillment constraints")
    
facility.optimize()
facility.printAttr('X')
    


