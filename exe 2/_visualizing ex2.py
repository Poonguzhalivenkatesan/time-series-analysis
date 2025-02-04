#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load in the CSV file (adjust the file path accordingly)
sales_data = pd.read_csv(r"C:\Users\Lenovo\Downloads\supermarket_sales - Sheet1.csv")

# Check the first few rows of the dataset
print(sales_data.head())

# Convert the 'Date' column to datetime format
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Set the 'Date' column as the index for time series analysis
sales_data.set_index('Date', inplace=True)

# Check for missing values
print(sales_data.isnull().sum())

# Create a line plot of sales data over time
plt.figure(figsize=(10, 6))
# Access the correct sales column, likely 'Total' or 'sales'
plt.plot(sales_data.index, sales_data['Total'], label='Sales (USD)', color='b')  
plt.xlabel('Date')
plt.ylabel('Sales (USD)')
plt.title('Supermarket Sales Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()


# In[5]:


sales_by_product = sales_data.groupby([sales_data.index, 'Product line'])['Total'].sum().unstack()

# Plot the sales for each product over time
plt.figure(figsize=(12, 6))
sales_by_product.plot(kind='line')
plt.title('Sales by Product Over Time')
plt.xlabel('Date')
plt.ylabel('Sales (USD)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Product')
plt.show()


# In[6]:


sales_pivot = sales_data.pivot_table(index=sales_data.index.date, columns='Product line', values='Total', aggfunc='sum')  # Changed 'Item' to 'Product line'

# Plot the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(sales_pivot, cmap='YlGnBu', annot=True, fmt='.0f', linewidths=.5)
plt.title('Sales Heatmap by Product and Date')
plt.xlabel('Product')
plt.ylabel('Date')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[7]:


# Group by store and sum sales
sales_by_store = sales_data.groupby('Branch')['Total'].sum()

# Plot the bar plot
plt.figure(figsize=(8, 6))
sales_by_store.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Store')
plt.xlabel('Store')
plt.ylabel('Sales (USD)')
plt.tight_layout()
plt.show()


# In[ ]:




