# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 10:51:35 2022

@author: karthi.vignes
"""

import random
import pandas as pd
ITEMS = 15

class Bin:
	def __init__(self):
		self.list = []

	def addItem(self, item):
		self.list.append(item)

	def removeItem(self, item):
		self.list.remove(item)

	def sum(self):
		total = 0
		for elem in self.list:
			total += elem
		return total

	def show(self):
		return self.list

def next_fit(item_list, bin_capacity=1):
    list_bins = []
    list_bins.append(Bin())
    remain = bin_capacity
    sum_item = 0
    for i in item_list:
        sum_item += i
        if i > remain:  # Overflow. Need new bin
            list_bins.append(Bin())  # Create new bin
            remain = bin_capacity  # All space is available in it
        list_bins[-1].addItem(i)  # Add box in this bin
        remain -= i
            
    result_items = []
    for bin in list_bins:
        result_items.append(bin.show())
      
    waste = len(list_bins) - sum(item_list)
    return result_items, waste

random.seed(2)
items = [random.random() for i in range(ITEMS)]
result, waste = next_fit(items)
result_dict = dict(zip([i for i in range(len(result))],result))
result_df = pd.DataFrame.from_dict(result_dict, orient='index')
print(result_df)
print(f"Excess bin capacity: {waste}")