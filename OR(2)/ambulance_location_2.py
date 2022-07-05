# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 20:49:46 2022

@author: karthi.vignes
"""

import pandas as pd
M = 3

distances = pd.read_excel('final.xlsx', 'Distances')
distances.drop('District', axis=1, inplace=True)
population = pd.read_excel('final.xlsx', 'Population')
ambulance_districts = []

#data
population = population['Population']

for i in range(M): # run m times
    best_dis = -1
    best_firefighting_times = 10000000000000
    for j in range(len(distances.index)):  # calculate the weighted-firefighting time for each district
        weighted_distance = distances[j+1]*population
        
        if max(weighted_distance) < best_firefighting_times and j not in ambulance_districts:
            best_dis = j
            best_firefighting_times = max(weighted_distance)
    ambulance_districts.append(best_dis)

# calculate objective value
min_distance = []
for i in range(len(distances.index)):
    min_dist = 100000
    for j in ambulance_districts:
        if distances[i+1][j] < min_dist:
            min_dist = distances[i+1][j]
    min_distance.append(min_dist)
    
weighted_distances = []
for amb_dist in ambulance_districts:
    weighted_distances.append(distances[amb_dist+1]*population)
    wd_df = pd.concat(weighted_distances, axis=1)
print(wd_df)

obj = max(pd.DataFrame(min_distance)[0]*population)
    
    

    