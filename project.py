import numpy as np
import pandas as pd

#importing the csv files into data frames

sales_data = pd.read_csv('sales data-set.csv')

stores_data = pd.read_csv('stores data-set.csv')

features_data = pd.read_csv('Features data set.csv')

#checking input csv files worked

print (sales_data.head())

print (stores_data.head())

print (features_data.head())



