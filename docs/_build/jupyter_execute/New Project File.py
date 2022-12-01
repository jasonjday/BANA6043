#!/usr/bin/env python
# coding: utf-8

# # Final Project - Group 1
# 1. [Introduction](#Section1)
# 2. [Packages/Libraries Required](#Section2)
# 3. [Exploratory Data Analysis](#Section3)
# 4. [Summary](#Section4)
# 
# ## Introduction <a name="Section1"></a>
# We believe Regork can increase the effectiveness of their campaigns through identifying the most effective campaign for the right customer, at the right time. Improving the efficiency of campaigns helps to first lift sales. But campaigns also help build brand awareness and customer loyalty. By optimizing our campaign schedule, we believe Regork will see a higher return on investment.
# 
# Some use promotional campaigns during the holidays while others such as Regork have campaigns that occur year-round. We wanted to evaluate the effectiveness of Regork’s campaigns by determining the top campaigns run by Regork and figuring out how to improve them. Our focus was to figure out how these campaigns affected sales, departments and whether it’s better to have year-round campaigns or holiday focused ones. <br>
# For this project we used the [completejourney](https://bradleyboehmke.github.io/completejourney/articles/completejourney.html) data to answer our business problem. The data available on transactions, demographics, products and campaigns were combined to create one large data frame. Our group determined the campaigns that generate the highest revenue by finding the sum of sales for each campaign. Campaigns 18, 13 and 8 were found to be the "best" campaigns. Afterwards, we took a deeper dive into these three campaigns.  

# ## Packages/Libraries Required <a name="Section2"></a>
# These packages/libraries are used in this project.

# In[1]:


import pandas as pd               #Used for data manipulation, tidying data and conditional statements
import bokeh.io                   #bokeh is the main plotting package (submodules of bokeh must be explicitly imported)
import bokeh.models               #bokeh.models helps turn dataframes and dictionaries into easily transformable data
import bokeh.plotting             #this is the primary tool used to assemble plots
import bokeh.transform            #function for computations such as a cumulative sum function
bokeh.io.output_notebook()        #Enable viewing Bokeh plots in the notebook and interactive
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
campaigns = cj_data['campaigns']


# Once the completejourney data was imported into Python, the next step was to tidy the data. We were interested in discovering trends related to campaigns and how it affected sales. Therefore, we started with merging campaigns, demographics, transactions and products. 

# In[3]:


campaigns.columns.intersection(transactions.columns) #Checks which columns have the same heading in both datasets


# In[4]:


df1= (
    campaigns
    .merge(demographics, how='inner', on='household_id')
    .merge(transactions, how='inner', on='household_id')
)
df2= (
   df1
   .merge(products, how='inner', on='product_id')
)
coupons= (
    cj_data['coupon_redemptions']
    .merge(cj_data['demographics'], how='inner', on='household_id')
    .merge(cj_data['campaign_descriptions'], how='inner', on='campaign_id')
)
coupon_transactions = (
    cj_data['coupon_redemptions']
    .merge(cj_data['coupons'], how='inner', on='campaign_id')
)
test =(
    cj_data['campaign_descriptions']
    .merge(cj_data['coupon_redemptions'], how='inner', on='campaign_id')
)


# In[5]:


datetimes = pd.to_datetime(coupon_transactions['redemption_date'])
coupon_transactions['day'] = datetimes.dt.day
coupon_transactions['month'] = datetimes.dt.month
coupon_transactions['year'] = datetimes.dt.year

coupon_redemptions = (
coupon_transactions
    .groupby('month')['redemption_date'].count()
)
coupon_redemptions = coupon_redemptions.to_frame()


# In[6]:


coupon_transactions.loc[coupon_transactions['campaign_id'] == 18]


# In[7]:


campaign13_transactions = (
    coupon_transactions
    .query('campaign_id==18')
)
campaign13_redemptions = (
campaign13_transactions
    .groupby('month')['redemption_date'].count()
)
campaign13_redemptions = campaign13_redemptions.to_frame()
campaign13_redemptions


# In[8]:


top_campaign_transactions = (
    coupon_transactions
    .query('campaign_id==18' or 'campaign_id==13' or 'campaign_id==8')
)
top_campaign_redemptions = (
top_campaign_transactions
    .groupby('month')['redemption_date'].count()
)
top_campaign_redemptions = top_campaign_redemptions.to_frame()


# In[9]:


top_campaign_redemptions


# ### Which campaigns sold the most products?
# The first step we took to evaluate the effectiveness of campaigns was to find out the total sales achieved through each campaign.

# In[10]:


df_campaigns = df2.groupby(['campaign_id'],as_index=False).agg({'sales_value':'sum'}).sort_values(by = 'sales_value', ascending=False)

ax =(df_campaigns
    .sort_values('sales_value')
    .plot(x='campaign_id', y='sales_value', kind='barh', title='Revenue Earned Through Each Campaign', figsize=(4,7),color='green', legend = False, xlabel='Campaign')
);
ax.set_xlabel('Sales');


# Looking at the bar chart above it is clear that campaigns 18, 13 and 8 generated the highest sales. Let's take a deeper dive into these three campaigns.

# ### Which departments were affected by campaigns 18, 13 & 8?
# In this section we determined the departments that brought in the most revenue within these the top 3 campaigns.

# In[11]:


df_campaigns_18 = df2.loc[(df2['campaign_id']==18)] 
df_department_18 = df_campaigns_18.groupby(['department'],as_index=False).agg({'sales_value':'sum'}).sort_values(by = 'sales_value', ascending=True)
df_department_18 = df_department_18[~df_department_18['department'].isin(['MISCELLANEOUS', 'COUPON'])]


# In[12]:


df_campaigns_13 = df2.loc[(df2['campaign_id']==13)] 
df_department_13 = df_campaigns_13.groupby(['department'],as_index=False).agg({'sales_value':'sum'}).sort_values(by = 'sales_value', ascending=True)
df_department_13 = df_department_13[~df_department_13['department'].isin(['MISCELLANEOUS', 'COUPON'])]


# In[13]:


df_campaigns_8 = df2.loc[(df2['campaign_id']==8)] 
df_department_8 = df_campaigns_8.groupby(['department'],as_index=False).agg({'sales_value':'sum'}).sort_values(by = 'sales_value', ascending=True)
df_department_8 = df_department_8[~df_department_8['department'].isin(['MISCELLANEOUS', 'COUPON'])]
df_department_8['sales_value'].mean()


# In[14]:


df_campaigns_18 = df2.loc[(df2['campaign_id']==18)] 
df_campaigns_13 = df2.loc[(df2['campaign_id']==13)] 
df_campaigns_8 = df2.loc[(df2['campaign_id']==8)] 

df_department_18 = df_campaigns_18.groupby(['department'],as_index=False).agg({'sales_value':'sum'}).nlargest(15, 'sales_value').sort_values(by = 'sales_value', ascending=True)
df_department_18 = df_department_18[~df_department_18['department'].isin(['MISCELLANEOUS', 'COUPON'])]

df_department_13 = df_campaigns_13.groupby(['department'],as_index=False).agg({'sales_value':'sum'}).nlargest(15, 'sales_value').sort_values(by = 'sales_value', ascending=True)
df_department_13 = df_department_13[~df_department_13['department'].isin(['MISCELLANEOUS', 'COUPON'])]

df_department_8 = df_campaigns_8.groupby(['department'],as_index=False).agg({'sales_value':'sum'}).nlargest(15, 'sales_value').sort_values(by = 'sales_value', ascending=True)
df_department_8 = df_department_8[~df_department_8['department'].isin(['MISCELLANEOUS', 'COUPON'])]


# In[15]:


fig, ax_array = plt.subplots(1, 3, figsize=(12, 8), constrained_layout=True)
ax1 = ax_array[0]  
ax2 = ax_array[1]  
ax3 = ax_array[2]  
# plot 1
ax1.barh('department','sales_value', data=df_department_18, color = 'green')
ax1.set_ylabel('Department')
ax1.set_title('Sales generated per department in Cam. 18')
# plot 2
ax2.barh('department','sales_value', data=df_department_13, color = 'green')
ax2.set_title('Sales generated per department in Cam. 13')
# plot 3
ax3.barh('department','sales_value', data=df_department_8, color = 'green')
ax3.set_title('Sales generated per department in Cam. 8');


# It looks like certain departments such as Grocery and Drug GM generated the most revenue while departments such as whole sales and Postal Center did not generate any revenue at all. Looking at the above graphs Regork will benefit from introducing campaigns focusing more on departments Deli through Grocery and eliminate campaigns for some of the low yielding departments.

# ### Coupon Redemptions by Age Group
# Now that we can see which campaigns are most effective, we can look at what customers are most valuable to target these campaigns towards.

# In[16]:


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


# ### Campaign sales for each age group in 2017
# Finally sales patterns for campaigns 18, 13 and 8 according to each age group was observed.

# In[17]:


df_campaigns_18['Transaction_Time'] = pd.to_datetime(df_campaigns_18['transaction_timestamp']).dt.time
df_campaigns_18['Transaction_Date'] = pd.to_datetime(df_campaigns_18['transaction_timestamp']).dt.date
cam18_age = df_campaigns_18.groupby(['age','Transaction_Date'],as_index=False).agg({'sales_value':'sum'})

df_campaigns_13['Transaction_Time'] = pd.to_datetime(df_campaigns_13['transaction_timestamp']).dt.time
df_campaigns_13['Transaction_Date'] = pd.to_datetime(df_campaigns_13['transaction_timestamp']).dt.date
cam13_age = df_campaigns_13.groupby(['age','Transaction_Date'],as_index=False).agg({'sales_value':'sum'})

df_campaigns_8['Transaction_Time'] = pd.to_datetime(df_campaigns_8['transaction_timestamp']).dt.time
df_campaigns_8['Transaction_Date'] = pd.to_datetime(df_campaigns_8['transaction_timestamp']).dt.date
cam8_age = df_campaigns_8.groupby(['age','Transaction_Date'],as_index=False).agg({'sales_value':'sum'})


# In[18]:


from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import jitter
from bokeh.layouts import row

# create color mapper
color_mapper = bokeh.transform.factor_cmap(
    'age', 
    palette=['red', 'blue','green','orange','purple','grey'], 
    factors=cam18_age['age'].unique()
    )

# plot 7
source1 = ColumnDataSource(cam18_age)
ax7 = figure(sizing_mode="stretch_width",
    frame_height=1000,
           x_axis_type='datetime',
           title="Campaign 18 sales by each Age Group Over the Year")

ax7.scatter(x='Transaction_Date', y=jitter('sales_value', width=0.6, range=ax7.y_range),  source=source1,
         fill_color=color_mapper,
    line_color=color_mapper,
    legend_field='age'        
)
ax7.yaxis.axis_label = 'Sales'
ax7.legend.title = "Age Group"

# display legend in top left corner (default is top right corner)
ax7.legend.location = "top_left"

tooltips = [("Sales","@sales_value")]
hover = bokeh.models.HoverTool(tooltips=tooltips, mode='mouse')
ax7.add_tools(hover)

# plot 8
source2 = ColumnDataSource(cam13_age)
ax8 = figure(sizing_mode="stretch_width",
    frame_height=1000,
           x_axis_type='datetime',
           title="Campaign 13 sales by each Age Group Over the Year")

ax8.scatter(x='Transaction_Date', y=jitter('sales_value', width=0.6, range=ax8.y_range),  source=source2,
         fill_color=color_mapper,
    line_color=color_mapper
)

tooltips = [("Sales","@sales_value")]
hover = bokeh.models.HoverTool(tooltips=tooltips, mode='mouse')
ax8.add_tools(hover)

# plot 9
source3 = ColumnDataSource(cam8_age)
ax9 = figure(sizing_mode="stretch_width",
    frame_height=1000,
           x_axis_type='datetime',
           title="Campaign 8 sales by each Age Group Over the Year")

ax9.scatter(x='Transaction_Date', y=jitter('sales_value', width=0.6, range=ax9.y_range),  source=source3,
         fill_color=color_mapper,
    line_color=color_mapper
)

tooltips = [("Sales","@sales_value")]
hover = bokeh.models.HoverTool(tooltips=tooltips, mode='mouse')
ax9.add_tools(hover)

# put the results in a row and show
bokeh.io.show(row(ax7,ax8,ax9))


# From the two above plots, it is clear that age group 45-54 brings in the most revenue for each campaign and redeems the most coupons. Age groups 55 and above and the youngest age group (19-24) are in the lower sales range while 25-44 age groups are in the middle. Regork should prioritize the 45-54 age group when introducing new campaigns in order to increase sales and capitalize on dollars invested.

# ### Coupon Redemptions Over Time
# We can now look at what times of the year coupons are most used.

# In[19]:


coupon_redemptions.plot(
    kind='line',
    title='Coupon Redemption over time',
    ylabel='Redemption Count',
    xlabel='Month',
    figsize=(15,3)
);


# In[20]:


campaign_18_redemptions.plot(
    kind='line',
    title='Coupon Redemption over time',
    ylabel='Redemption Count',
    xlabel='Month',
    figsize=(15,3)
);


# ## Summary <a name="Section4"></a>
# The second paragraph text

# In[96]:


married_value = (
    df1
    .groupby(['marital_status'],as_index=False)
    .agg({'sales_value': 'mean'})
)
married_value


# In[97]:


married_value.plot.bar(x='marital_status', y='sales_value')


# In[98]:


salary_value = (
    df1
    .groupby(['income'],as_index=False)
    .agg({'sales_value': 'mean'})
    .sort_values('sales_value')
)
salary_value


# In[99]:


salary_value.plot.bar(x='income', y='sales_value')


# In[100]:


homeowner_value = (
    df1
    .groupby(['home_ownership'],as_index=False)
    .agg({'sales_value':'mean'})
)
homeowner_value


# In[101]:


homeowner_value.plot.bar(x='home_ownership', y='sales_value')


# In[ ]:





# In[ ]:




