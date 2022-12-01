#!/usr/bin/env python
# coding: utf-8

# # Introduction

# ## Meet Our Team

# <table style="width:100%">
#   <tr>
#     <td style="text-align: center">  <img src="img/elayna_headshot.png"></td>
#     <td style="text-align: center">  <img src="img/hashani_headshot.png"></td>
#     <td style="text-align: center">  <img src="img/jason_headshot.png"></td>
#   </tr>
#   <tr>
#     <td style="text-align: center">Elayna Berry</td>
#     <td style="text-align: center">Hashani DeSilva</td>
#     <td style="text-align: center">Jason Day</td>
#   </tr>
# </table>

# ## Regork's Opportunity

# Regork has compiled data around campaigns, transactions, and customers; however, this data has not been leveraged to identify the full impact of campaigns on product sales. This can allow our marketing teams to leverage their promotional dollars most effectively. We can do this by identifying which campaigns are most effective and least effective, when they bring and least volume of sales in, and which customers that use coupons provide our business the most value.
# 
# The visualizations, found in the navigation to the left, will discuss our analysis and our proposal.
# 
# ====
# 
# We believe Regork can increase the effectiveness of their campaigns through identifying the most effective campaign for the right customer, at the right time. Improving the efficiency of campaigns helps to first lift sales. But campaigns also help build brand awareness and customer loyalty. By optimizing our campaign schedule, we believe Regork will see a higher return on investment.
# 
# Some use promotional campaigns during the holidays while others such as Regork have campaigns that occur year-round. We wanted to evaluate the effectiveness of Regork’s campaigns by determining the top campaigns run by Regork and figuring out how to improve them. Our focus was to figure out how these campaigns affected sales, departments and whether it’s better to have year-round campaigns or holiday focused ones. <br>
# For this project we used the [completejourney](https://bradleyboehmke.github.io/completejourney/articles/completejourney.html) data to answer our business problem. The data available on transactions, demographics, products and campaigns were combined to create one large data frame. Our group determined the campaigns that generate the highest revenue by finding the sum of sales for each campaign. Campaigns 18, 13 and 8 were found to be the "best" campaigns. Afterwards, we took a deeper dive into these three campaigns.  

# ## Required Packages and Libraries

# To properly reproduce these visualizations you will need to use the following packages and libraries:

# In[1]:


import pandas as pd               #Used for data manipulation, tidying data and conditional statements
import bokeh.io                   #bokeh is the main plotting package (submodules of bokeh must be explicitly imported)
import bokeh.models               #bokeh.models helps turn dataframes and dictionaries into easily transformable data
import bokeh.plotting             #this is the primary tool used to assemble plots
import bokeh.transform            #function for computations such as a cumulative sum function
bokeh.io.output_notebook()        #Enable viewing Bokeh plots in the notebook and interactive
import matplotlib.pyplot as plt   #Data visualization dictionary
import numpy as np                #Foundational computing package that works faster than Python


# In[2]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab')


# In[ ]:




