import pandas as pd

def load_and_clean_data():
    """Load all three CSV files and clean them."""
    
    # Load the files
    sales_data = pd.read_csv('DATA/sales data-set.csv')
    stores_data = pd.read_csv('DATA/stores data-set.csv')
    features_data = pd.read_csv('DATA/Features data set.csv')
    
    print("Files loaded successfully!")
    
    # Convert Date columns to datetime
    sales_data['Date'] = pd.to_datetime(sales_data['Date'], format='%d/%m/%Y')
    features_data['Date'] = pd.to_datetime(features_data['Date'], format='%d/%m/%Y')
    
    print("Dates converted to datetime format!")
    
    # Cleaning the features_data (I am doing this by fill NaN values with mean)
    features_data['MarkDown1'].fillna(features_data['MarkDown1'].mean(), inplace=True)
    features_data['MarkDown2'].fillna(features_data['MarkDown2'].mean(), inplace=True)
    features_data['MarkDown3'].fillna(features_data['MarkDown3'].mean(), inplace=True)
    features_data['MarkDown4'].fillna(features_data['MarkDown4'].mean(), inplace=True)
    features_data['MarkDown5'].fillna(features_data['MarkDown5'].mean(), inplace=True)
    features_data['CPI'].fillna(features_data['CPI'].mean(), inplace=True)
    features_data['Unemployment'].fillna(features_data['Unemployment'].mean(), inplace=True)
    
    print("Data cleaned successfully!")
    
    return sales_data, stores_data, features_data