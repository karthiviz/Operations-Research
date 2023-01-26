# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 19:15:16 2023

@author: karthi.vignes
"""

import pandas as pd
from gurobipy import GRB, Model
import gurobipy_pandas as gppd

projects = pd.read_csv("data/projects.csv", index_col="project")
teams = pd.read_csv("data/teams.csv", index_col="team")

allowed_pairs = (
    pd.merge(
        projects.reset_index(),
        teams.reset_index(),
        how='cross',
    )
    .query("difficulty <= skill")
    .set_index(["project", "team"])
)

print(
    f"Model will have {len(allowed_pairs)} variables"
    f" (out of a possible {len(projects) * len(teams)})"
)

model = Model()
model.ModelSense = GRB.MAXIMIZE
x = gppd.add_vars(model, allowed_pairs, 
            vtype=GRB.BINARY, 
            obj="value", 
            name="x")

total_resource = (
    (projects["resource"] * x)
    .groupby("team").sum()
)

capacity_constraints = gppd.add_constrs(
    model, total_resource, GRB.LESS_EQUAL, teams["capacity"],
    name='capacity',
)

allocate_once = gppd.add_constrs(
    model, x.groupby('project').sum(),
    GRB.LESS_EQUAL, 1.0, name="allocate_once",
)

model.optimize()

assignments = (
    x.gppd.X.to_frame()
    .query("x >= 0.9").reset_index()
    .groupby("team").agg({"project": list})
)

print(assignments)