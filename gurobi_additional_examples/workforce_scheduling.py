# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 19:07:15 2023

@author: karthi.vignes
"""

from gurobipy import GRB, Model
import pandas as pd
import gurobipy_pandas as gppd

preferences = pd.read_csv(
    "data/preferences.csv",
    parse_dates=["Shift"],
    index_col=['Worker', 'Shift']
)

shift_requirements = pd.read_csv(
    "data/shift_requirements.csv",
    parse_dates=["Shift"],
    index_col="Shift"
)

m = Model()
df = (
    preferences
    .gppd.add_vars(
        m, name="assign", vtype=GRB.BINARY, obj="Preference",
        index_formatter={"Shift": lambda index: index.strftime('%a%d')},
    )
)

shift_cover = gppd.add_constrs(
    m,
    df['assign'].groupby('Shift').sum(),
    GRB.EQUAL,
    shift_requirements["Required"],
    name="shift_cover",
    index_formatter={"Shift": lambda index: index.strftime('%a%d')},
)

m.optimize()
solution = df['assign'].gppd.X

shift_table = solution.unstack(0).fillna("-").replace({0.0: "-", 1.0: "Y"})
print(shift_table)
