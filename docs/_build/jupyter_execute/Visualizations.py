#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# ## Required Packages and Libraries

# To properly reproduce these visualizations you will need to use the following packages and libraries:

# In[1]:


import pandas as pd               #Used for data manipulation, tidying data and conditional statements
import matplotlib.pyplot as plt   #Data visualization dictionary
import numpy as np  


# ## Data Prep & Cleaning

# Since our focus is on how campaigns affected sales the following data frames were imported into Python:

# In[2]:


from completejourney_py import get_data

cj_data = get_data()
transactions = cj_data['transactions']
demographics = cj_data['demographics']
products = cj_data['products']
campaigns = cj_data['campaigns']


# Once the completejourney data was imported into Python, the next step was to tidy the data. We were interested in discovering trends related to campaigns and how it affected sales. Therefore, we started with merging campaigns, demographics, transactions and products. 

# In[3]:


# merge campaigns, demographics, transactions on household_id
df1 = (
    campaigns
    .merge(demographics, how='inner', on='household_id')
    .merge(transactions, how='inner', on='household_id')
)

# merging dataframe created above with products on product_id
df2 = (
   df1
   .merge(products, how='inner', on='product_id')
)

# merge coupon_redmptions with domepgraphics on household_id and campaign_descriptions on campaign_id
coupons = (
    cj_data['coupon_redemptions']
    .merge(cj_data['demographics'], how='inner', on='household_id')
    .merge(cj_data['campaign_descriptions'], how='inner', on='campaign_id')
)

# merge coupon_redemptions with coupons on campaign_id
coupon_transactions = (
    cj_data['coupon_redemptions']
    .merge(cj_data['coupons'], how='inner', on='campaign_id')
)


# In[4]:


datetimes = pd.to_datetime(coupon_transactions['redemption_date'])
coupon_transactions['day'] = datetimes.dt.day
coupon_transactions['month'] = datetimes.dt.month
coupon_transactions['year'] = datetimes.dt.year

coupon_redemptions = (
coupon_transactions
    .groupby('month')['redemption_date'].count()
)
coupon_redemptions = coupon_redemptions.to_frame()


# ## Visualizations

# ### Which campaigns sold the most products?

# The first step we took to evaluate the effectiveness of campaigns was to find out the total sales achieved through each campaign.

# In[5]:


df_campaigns = df2.groupby(['campaign_id'],as_index=False).agg({'sales_value':'sum'}).sort_values(by = 'sales_value', ascending=False)

ax =(df_campaigns
    .sort_values('sales_value')
    .plot(x='campaign_id', y='sales_value', kind='barh', title='Revenue Earned Through Each Campaign', figsize=(4,7),color='green', legend = False, xlabel='Campaign')
);
ax.set_xlabel('Sales');


# Looking at the bar chart above it is clear that campaigns 18, 13 and 8 generated the highest sales. Let's take a deeper dive into these three campaigns.

# ### Coupon Redemptions Over Time

# We can now look at what times of the year coupons are most used.

# In[6]:


coupon_redemptions.plot(
    kind='line',
    title='Coupon Redemption over time',
    ylabel='Redemption Count',
    xlabel='Month',
    figsize=(15,3)
);


# ### Coupon Redemptions by Age Group

# Now that we can see which campaigns are most effective, we can look at what customers are most valuable to target these campaigns towards.

# In[7]:


redemptions = (
coupons
    .groupby('age')['redemption_date'].count()
)
redemptions = redemptions.to_frame()
redemptions.plot(
    kind='bar',
    title='Coupon Redemptions by Age',
    ylabel='Redemption Count',
    xlabel='Age Group',
);


# Sales patterns for campaigns 18, 13 and 8 according to each age group was observed.

# ### Sales Value by Demographic

# In[8]:


married_value = (
    df1
    .groupby(['marital_status'],as_index=False)
    .agg({'sales_value': 'mean'})
)
married_value


# In[9]:


married_value.plot.bar(x='marital_status', y='sales_value');


# In[10]:


salary_value = (
    df1
    .groupby(['income'],as_index=False)
    .agg({'sales_value': 'mean'})
    .sort_values('sales_value')
)
salary_value


# In[11]:


salary_value.plot.bar(x='income', y='sales_value');


# In[12]:


homeowner_value = (
    df1
    .groupby(['home_ownership'],as_index=False)
    .agg({'sales_value':'mean'})
)
homeowner_value


# In[13]:


homeowner_value.plot.bar(x='home_ownership', y='sales_value');


# In[14]:


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


# # Environment

# In[15]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab')

