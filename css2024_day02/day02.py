# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:34 2024

@author: Phenyo Modise
"""
import pandas as pd
df=pd.read_csv("country_data_index.csv")
df=pd.read_csv("data_02/country_data_index.csv")
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv("data_02/country_data_index.csv",header=None, names= column_names)
print(column_names)