#!/usr/bin/env python
# coding: utf-8

# In[4]:


# import csv


# In[8]:


# with open('bmi_and_life_expectancy.csv', 'w', newline='') as f:
    
# # write / create csv file
       
#     fieldnames = ['1', '2', '3']
#     thewriter = csv.DictWriter(f, fieldnames=fieldnames)
#     thewriter.writeheader()
#     thewriter.writerow({'1':'', '2':'', '3':''})


# You'll need to complete each of the following steps:
# 1. Load the data
# 
# The data is in the file called "bmi_and_life_expectancy.csv".
# Use pandas read_csv to load the data into a dataframe (don't forget to import pandas!)
# Assign the dataframe to the variable bmi_life_data.
# 2. Build a linear regression model
# 
# Create a regression model using scikit-learn's LinearRegression and assign it to bmi_life_model.
# Fit the model to the data.
# 3. Predict using the model
# 
# Predict using a BMI of 21.07931 and assign it to the variable laos_life_exp.

# In[5]:


import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


# In[9]:


# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')

# x1 = bmi_life_data.iloc[:,2].values.reshape(-1,1)
# y1= bmi_life_data.iloc[:,1]
x = bmi_life_data[['BMI']] 
y = bmi_life_data[['Life expectancy']]


# In[38]:


# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model

bmi_life_model = LinearRegression()
bmi_life_model.fit(x, y)


# In[41]:


# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict([[21.07931]])
print(laos_life_exp)


# In[ ]:




