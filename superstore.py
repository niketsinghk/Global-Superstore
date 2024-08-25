import pandas as pd

def load_data():
    # Load the dataset
    df = pd.read_csv("global_superstore_2016.csv", encoding='latin1')

    # Handle missing data and data types
    df['Order Date'] 
    df['Ship Date'] 
    
    # Clean the 'Sales' and 'Profit' columns
    df['Sales'] 
    df['Profit'] 

    return df


def sales_by_category(df):
    # Group by 'Category' and sum the 'Sales'
    category_sales = df.groupby('Category')['Sales'].sum()
    return category_sales

def filter_by_category(df, category):
    # Filter the DataFrame by a specific category
    filtered_data = df[df['Category'] == category]
    return filtered_data
