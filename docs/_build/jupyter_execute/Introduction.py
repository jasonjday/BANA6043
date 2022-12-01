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

# Regork has compiled data around campaigns, transactions, coupon redemption, and customers. We believe Regork can increase the effectiveness of their campaigns through identifying the most effective campaign for the right customer, at the right time. Improving the efficiency of campaigns helps to first lift sales. But campaigns also help build brand awareness and customer loyalty. By optimizing our campaign schedule, we believe Regork will see a higher return on investment.
# 
# Some use promotional campaigns during the holidays while others, such as, Regork have campaigns that occur year-round. We evaluate the effectiveness of Regork’s campaigns by determining the top campaigns run by Regork and figuring out how to improve them. Our focus is to figure out how these campaigns affected sales, departments and whether it’s better to have year-round campaigns or holiday focused ones.
# 
# For this project we used the [completejourney](https://bradleyboehmke.github.io/completejourney/articles/completejourney.html) data to answer our business problem. The data available on transactions, demographics, products and campaigns were combined to create one large data frame. Our group determined the campaigns that generate the highest revenue by finding the sum of sales for each campaign. We will discuss our findings in the Exploratory Data and Summary Sections.
# 

# # Environment

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -p jupyterlab')

