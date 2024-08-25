import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import superstore

# Load the data
data = superstore.load_data()

# Title of the app
st.title("Superstore Data Analysis")

# Display the dataset
st.header("Dataset Overview")
st.write(data.head())

# Example visualization: Sales by Category
st.header("Sales by Category")
category_sales = superstore.sales_by_category(data)
st.bar_chart(category_sales)

# Example interaction: Filter by Category
st.header("Filter by Category")
categories = data['Category'].unique()
selected_category = st.selectbox("Select a Category", categories)
filtered_data = superstore.filter_by_category(data, selected_category)
st.write(filtered_data)
