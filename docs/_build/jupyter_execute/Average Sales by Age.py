#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd               #Used for data manipulation, tidying data and conditional statements
import matplotlib.pyplot as plt   #Data visualization dictionary
import numpy as np                #Foundational computing package that works faster than Python


# ## Exploratory Data Analysis <a name="Section3"></a>
# Since our focus is on how campaigns affected sales the following data frames were imported into Python:

# In[2]:


from completejourney_py import get_data

cj_data = get_data()
transactions = cj_data['transactions']
demographics = cj_data['demographics']
products = cj_data['products']
coupons = cj_data['coupons']
coupon_redemptions = cj_data['coupon_redemptions']
campaigns = cj_data['campaigns']
campaign_descriptions = cj_data['campaign_descriptions']


# Once the completejourney data was imported into Python, the next step was to tidy the data. We were interested in discovering trends related to campaigns and how it affected sales. Therefore, we started with merging campaigns, demographics, transactions and products. 

# In[3]:


df1 = (
    campaigns
    .merge(demographics, how='inner', on='household_id')
    .merge(transactions, how='inner', on='household_id')
)

# merge
df2 = (
   df1
   .merge(products, how='inner', on='product_id')
)


# In[4]:


age_group = (
df1
    .groupby(['age'])
    .agg({'sales_value': 'mean'})
)
age_group.plot(
    kind='bar',
    title='Average Sales by Age',
    ylabel='Average Sales Value',
    xlabel='Age Group',
);


# When considering the average sales made by each group, it is clear that people within the ages of 35-64 spend more money. Therefore, it would be beneficial for Regork to prioritize these age groups during promotional campaigns and coupon distributions.

# In[ ]:




