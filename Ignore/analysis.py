import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from data_cleaning import load_and_clean_data

# LOAD AND CLEAN DATA
print("\nLOADING AND CLEANING DATA")
sales_data, stores_data, features_data = load_and_clean_data()

# Check data
print("\nNaN values in features_data after cleaning:")
print(features_data.isnull().sum())

# MERGE DATA
print("\nMERGING DATA FRAMES")
merged_data = sales_data.merge(stores_data, on='Store', how='left')
merged_data = merged_data.merge(features_data, on=['Store', 'Date'], how='left')

print("✓ Data merged successfully")
print(f"Shape: {merged_data.shape[0]} rows, {merged_data.shape[1]} columns")

# FIX DUPLICATE IsHoliday COLUMNS
print("\nFIXING DUPLICATE COLUMNS")
if 'IsHoliday_x' in merged_data.columns and 'IsHoliday_y' in merged_data.columns:
    merged_data['IsHoliday'] = merged_data['IsHoliday_x']
    merged_data = merged_data.drop(['IsHoliday_x', 'IsHoliday_y'], axis=1)
    print("✓ IsHoliday columns merged")

# CREATE TOTAL MARKDOWN FEATURE
print("\nCREATING FEATURES")
merged_data['Total_MarkDown'] = (
    merged_data['MarkDown1'] + 
    merged_data['MarkDown2'] + 
    merged_data['MarkDown3'] + 
    merged_data['MarkDown4'] + 
    merged_data['MarkDown5']
)

# Reorder columns to put Total_MarkDown after MarkDown5
cols = merged_data.columns.tolist()
markdown5_index = cols.index('MarkDown5')
cols.remove('Total_MarkDown')
cols.insert(markdown5_index + 1, 'Total_MarkDown')
merged_data = merged_data[cols]

print("✓ Total_MarkDown column created and positioned")

# FINAL DATA INSPECTION
print("\nFINAL MERGED DATA PREVIEW")
print(merged_data.head())
print("\nColumn types:")
print(merged_data.info())

# EXPORT CLEANED DATA
print("\nEXPORTING DATA")
merged_data.to_csv('DATA/cleaned_merged_data.csv', index=False)
print("✓ Cleaned and merged data exported to 'DATA/cleaned_merged_data.csv'")

# ANALYSIS
#Store type analysis

#Which store type performs the bests

total_sales_by_type = merged_data.groupby('Type')['Weekly_Sales'].sum()
print ("total sales by store type:")
print(total_sales_by_type)

total_sales_by_type_sorted = merged_data.groupby('Type')['Weekly_Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales by Store Type (sorted):")

print(total_sales_by_type_sorted)

# Create a bar chart of this data


plt.figure(figsize=(10, 6))
total_sales_by_type_sorted.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Total Sales by Store Type', fontsize=16, fontweight='bold')
plt.xlabel('Store Type', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)

print("\nANALYSIS: HOLIDAY VS NON-HOLIDAY SALES")

holiday_average_sales = merged_data[merged_data['IsHoliday'] == True]['Weekly_Sales'].mean()
non_holiday_average_sales = merged_data[merged_data['IsHoliday'] == False]['Weekly_Sales'].mean()
sales_difference = holiday_average_sales - non_holiday_average_sales

print(f"Average sales during holidays: ${holiday_average_sales:,.2f}")
print(f"Average sales during non-holidays: ${non_holiday_average_sales:,.2f}")
print(f"Difference: ${sales_difference:,.2f}")

if sales_difference > 0:
    percentage_increase = (sales_difference / non_holiday_average_sales) * 100
    print(f"Holiday weeks have {percentage_increase:.1f}% higher sales")
else:
    percentage_decrease = abs(sales_difference / non_holiday_average_sales) * 100
    print(f"Holiday weeks have {percentage_decrease:.1f}% lower sales")
#now looking into what stores perfom best during holiday weeks