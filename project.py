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

print ("Removing the NaN values from features_data by calculating the mean:")

avg_markdown1= features_data['MarkDown1'].mean()
features_data['MarkDown1'].fillna(avg_markdown1, inplace=True)

avg_markdown2= features_data ['MarkDown2'].mean()
features_data['MarkDown2'].fillna(avg_markdown2, inplace=True)

avg_markdown3 = features_data ['MarkDown3'].mean()
features_data['MarkDown3'].fillna(avg_markdown3, inplace=True)

avg_markdown4= features_data ['MarkDown4'].mean()
features_data['MarkDown4'].fillna(avg_markdown4, inplace=True)

avg_markdown5= features_data ['MarkDown5'].mean()
features_data['MarkDown5'].fillna(avg_markdown5, inplace=True)

avg_CPI= features_data ['CPI'].mean()
features_data['CPI'].fillna(avg_CPI, inplace=True)

avg_unemployment= features_data ['Unemployment'].mean()
features_data['Unemployment'].fillna(avg_unemployment, inplace=True)

#Checking again for NaN values in all CSV files


#Checking Number of NaN values
print ("Number of NaN values in sales_data after cleaning")
print (sales_data.isnull().sum())
print ("Number of NaN values in stores_data after cleaning")
print (stores_data.isnull().sum())
print ("Number of NaN values in features_data after cleaning")
print (features_data.isnull().sum())




print ("now time for transforming")

#Transforming
#There are no date values for conversion in stores data frame
#phase one converting date to datetime object
#there was an issue with this so after some AI help I have found I need to add the dayfirst = true as is standard EU/UK Notation

print("Converting date column in sales_data to datetime object")
sales_data['Date'] = pd.to_datetime(sales_data['Date'], dayfirst=True)
print(sales_data.info())

print("Converting date column in features_data to datetime object")
features_data['Date'] = pd.to_datetime(features_data['Date'], dayfirst=True)
print(features_data.info())

#now to check for duplicates in the data frames

print("Checking for duplicates in sales_data:")
sales_duplicates = sales_data.duplicated().sum()
if sales_duplicates > 0:
    print("Yes, there are duplicates in sales_data")
else:
    print("No duplicates in sales_data")

print("Checking for duplicates in stores_data:")
stores_duplicates = stores_data.duplicated().sum()
if stores_duplicates > 0:
    print("Yes, there are duplicates in stores_data")
else:
    print("No duplicates in stores_data")

print("Checking for duplicates in features_data:")
features_duplicates = features_data.duplicated().sum()
if features_duplicates > 0:
    print("Yes, there are duplicates in features_data")
else:
    print("No duplicates in features_data")
#No duplicates were found in any data frame

#Merging and concatenating the data frames into a single data frame

df = sales_data.merge(stores_data, on='Store', how='left')
df= df.merge(features_data, on=['Store', 'Date'], how='left')

print (df.head())

#checking columns
print ("n===Types of Columns in merged data frame ===")
print (df.columns.tolist())
#checking values counts per column
print("\n=== Value counts per column ===")
print(df.info())
#there is two IsHoliday columns (X and Y) and AI has told me that these are the same column but pandas has issued an x and y to differentiate them. I will drop one of them.
#I have consulted AI for assistance with this

print("\n=== Merging IsHoliday columns ===")

if 'IsHoliday_x' in df.columns and 'IsHoliday_y' in df.columns:
    # Keep one IsHoliday column
    df['IsHoliday'] = df['IsHoliday_x']
df = df.drop(['IsHoliday_x', 'IsHoliday_y'], axis=1)

#checking if it worked
print (df.columns.tolist())
print(df.info())

print (df.head())

#calculating total markdowns

#create a new column for total markdowns

df['Total_MarkDown'] = df['MarkDown1'] + df['MarkDown2'] + df['MarkDown3'] + df['MarkDown4'] + df['MarkDown5']

print (df.head())

#I have now consulted AI to find out how to move the Total_Markdown column next to the MarkDowns

# Get current column order
cols = df.columns.tolist()

# Find the position after MarkDown5
markdown5_index = cols.index('MarkDown5')

# Remove Total_MarkDown from wherever it is
cols.remove('Total_MarkDown')

# Insert it right after MarkDown5
cols.insert(markdown5_index + 1, 'Total_MarkDown')

# Reorder the DataFrame
df = df[cols]

print("Columns reordered!")
print(df.columns.tolist())

print (df.head())

#Analysis time

print ("-----Analysis time-----")

#calculating the difference between Weeklysales in Non-Holiday and Holiday weeks
# 
# #creating two data frames one for holiday weeks and one for non-holiday weeks

holiday_average_sales = df[df['IsHoliday'] == True]['Weekly_Sales'].mean()

non_holiday_average_sales = df[df['IsHoliday'] == False]['Weekly_Sales'].mean()

sales_difference = holiday_average_sales - non_holiday_average_sales

print ("====Sales Analysis between Holiday and Non-Holiday Weeks====")

print("Average sales during holidays:", holiday_average_sales)
print("Average sales during non-holidays:", non_holiday_average_sales)
print("Difference:", sales_difference)

