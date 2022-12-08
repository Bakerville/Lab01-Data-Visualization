# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:53:34 2015

@author: nymph
"""


#################################### Read the data ############################
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import numpy as np
sns.set()

''' read_csv()
The read_csv() function in pandas package parse an csv data as a DataFrame data structure. What's the endpoint of the data?
The data structure is able to deal with complex table data whose attributes are of all data types. 
Row names, column names in the dataframe can be used to index data.
'''

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original", delim_whitespace = True, \
 header=None, names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin', 'car_name'])

data['mpg']
data.mpg
data.iloc[0,:]

print(data.shape)

################################## Enter your code below ######################

num_duplicate = data.duplicated().sum()

print("\nCau01:\n")

def check_duplicate():
 if num_duplicate == 0:
  print("So xe:", data.shape[0])
  print("So thuoc tinh:", data.shape[1])
 else:
  print("So xe:", data.shape[0]-num_duplicate)
  print("So thuoc tinh", data.shape[1])

check_duplicate()

print("\nCau02:\n")

pd. set_option('display.max_columns', None)

def get_producer(name):
 get_list = name.split(" ")
 return get_list[0]

data["producer"] = data["car_name"].apply(get_producer)

best_mpg = data.loc[data["mpg"].idxmax(), "car_name"]

print("The best mpg car: ", best_mpg, "\n")

def count_8_cylinders(x):
 return x[x==8.0].count()
most_8_cylinder_company = data.groupby(["producer"])["cylinders"].apply(count_8_cylinders).idxmax()

print("The company produced the most 8_cylinders_car:", most_8_cylinder_company, "\n")

name_3_cylinder_car = data.loc[data.cylinders==3.0,"car_name"]

print("Name of 3_cylinder_car: ")

for name in name_3_cylinder_car:
 print("- ", name)
