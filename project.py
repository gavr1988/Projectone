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



print ("information about data frame sales_data:")
#getting a technical summary of the data frame
print (sales_data.info())

#Cleaning the data

#Checking for NaN values in data frames

print ("Checking for NaN values in sales_data:")

if sales_data.isnull().any().any():
    print ("Yes, there are NaN values in stores_data")
else:
    print ("No, NaN in stores_data")

print ("Checking for NaN values in stores_data:")
if stores_data.isnull().any().any():
    print ("Yes, there are NaN values in stores_data")
else:
    print ("No NaN in stores_data")

print ("checking for NaN values in features_data:")
if features_data.isnull().any().any():
    print ("Yes, there are NaN values in features_data")
else:
    print ("No NaN in features_data")

#Now dealing with NaN values in data frames


print (features_data.isnull().sum())

