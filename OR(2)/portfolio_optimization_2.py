# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 11:01:36 2022

@author: karthi.vignes
"""

import pandas as pd
from gurobipy import *

stock_info = pd.read_excel('week4.xlsx', 'Stock information')
stocks = range(len(stock_info['Stock']))
price = stock_info['Price']
exp_price = stock_info['Expected price']
variance = stock_info['Variance of the price']
max_variance = 250000000

b_and_min_rev = pd.read_excel('week4.xlsx', 'Budget and min_exp_profit')
budget = b_and_min_rev['Budget']
min_rev = b_and_min_rev['Minimum expected profit']

pfolio_max = Model('pfolio_max')

s = [pfolio_max.addVar(lb=0, vtype=GRB.CONTINUOUS, name="s"+str(i+1)) for i in stocks]

pfolio_max.setObjective(quicksum((exp_price[i]-price[i]) * s[i] for i in stocks), GRB.MAXIMIZE)

pfolio_max.addConstr(quicksum(price[i]*s[i] for i in stocks) <= budget, "budget_limit")
pfolio_max.addConstr(quicksum(variance[i]*s[i]*s[i] for i in stocks) <= max_variance, "risk_limit")

pfolio_max.optimize()
pfolio_max.printAttr('X')