#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
# Load the dataset from a local path
# Replace 'path/to/your/beer_production.csv' with your actual dataset path
dataset_path = (r"C:\Users\Lenovo\Downloads\monthly-beer-production-in-austr.csv")
data = pd.read_csv(dataset_path, header=0, parse_dates=[0], index_col=0,  date_parser=pd.to_datetime)

# Show the first few rows of the dataset
print(data.head())
# Step 1: Plot the time series data
def plot_time_series(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title("Monthly Beer Production in Australia")
    plt.xlabel('Date')
    plt.ylabel('Beer Production (in Mega Litres)')
    plt.show()
# Plot the time series
plot_time_series(data)
# Step 2: Perform Augmented Dickey-Fuller (ADF) Test
def adf_test(data):
    result = adfuller(data)
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    print("Critical Values:")
    for key, value in result[4].items():
        print(f'    {key}: {value}')

    if result[1] < 0.05:
        print("The series is stationary (p-value < 0.05).")
    else:
        print("The series is not stationary (p-value > 0.05).")
# Perform the ADF Test
adf_test(data)
# Step 3: Rolling Statistics (Mean and Std)
def rolling_statistics(data):
    rolling_mean = data.rolling(window=12).mean()
    rolling_std = data.rolling(window=12).std()
    plt.figure(figsize=(10, 6))
    plt.plot(data, label="Original")
    plt.plot(rolling_mean, label="Rolling Mean", color='red')
    plt.plot(rolling_std, label="Rolling Std", color='green')
    plt.legend(loc="best")
    plt.title("Rolling Mean and Rolling Standard Deviation")
    plt.show()
# Visualize Rolling Statistics
rolling_statistics(data)


# In[ ]:





# In[ ]:




