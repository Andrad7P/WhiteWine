#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[15]:


get_ipython().system('pip install pandas')


# In[27]:


import pandas as pd
wine_df = pd.read_csv("datasets/White.csv")
wine_df.head(3)


# DataSet cleaning: 
# 
# From what I am able to gather the dataset is clean. I will be gather data from the world market of wine. 
# Everything seems to be properly annotated and filled out in regards to the information provided. 
# The features seem to be 'Name', 'Country', 'Region', 'Winery', 'Rating', 'NumberOfRatings', 'Price', 'Year')aset

# In[29]:


wine_df.columns
# provides columns


# In[31]:


wine_df.dtypes
# Making sure that data types are what you wnat them to be. 


# In[33]:


wine_df.index
#index values of our data sets


# In[ ]:


import pandas as pd
wine_df = pd.read_csv("datasets/White.csv")
wine_df.head(3)


# In[37]:


wine_df.shape
# 3,764 roll and we have 8 columns


# In[39]:


wine_df.describe()
# Basic statiscs that describes the data


# Features: Name, Country, Region, Winery, Rating, Number of ratings, Price, Year
# 
# ![image.png](attachment:a53b2f33-111e-46d2-8590-3d56ad033c6c.png)
# 

# In[41]:


wine_df.tail(3)


# df_france = df[df['Country'] == 'France']
# plt.figure(figsize=(10, 6))
# plt.plot
# 
# (df_france['Year'], df_france['Price'], marker='o', color='blue')
# 
# plt.title('Price
# Trend Over Time for France', fontsize=16)
# 
# plt.xlabel('Year', fontsize=14)
# plt.ylabel('Price (USD)', fontsize=14)
# 
# plt.grid(True)
# plt.show()

# In[ ]:


### The difference between .lc and .iloc


# In[ ]:


# Calculating the mean of the rating and price


# In[43]:


average_rating = wine_df["Rating"].mean()

average_price = wine_df["Price"].mean()

print(f"Average Rating: {average_rating}")
print(f"Average Price: ${average_price:.2f}")


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

wine_df = pd.read_csv('datasets/White.csv')

wine_df['Year'] = pd.to_numeric(wine_df['Year'], errors='coerce')
wine_df['Price'] = pd.to_numeric(wine_df['Price'], errors='coerce')
#similiar concept like in the example
average_price_per_year = wine_df.groupby('Year')['Price'].mean().reset_index()
# thrid time

plt.figure(figsize=(10, 6))
plt.plot(average_price_per_year['Year'], average_price_per_year['Price'], marker='o', color='black', linestyle='-', linewidth=2)
#easy labeling 
plt.xlabel('Year')
plt.ylabel('Average Price ($)')
plt.title('Average Wine Price Over the Years')
plt.tight_layout()
plt.show()



# In[ ]:


import os
print(os.path.abspath("datasets/White.csv"))


# 
#                                       Scatter Plot.............. Price vs Rating
# # plt.xlabel
# # plt.ylable
# import pandas as pd
# import matplotlib.pyplot as plt
# wine_df = pd.read_csv('datasets/White.csv')
# 
# https://mode.com/blog/python-data-visualization-libraries#matplotlib

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
wine_df = pd.read_csv('datasets/White.csv')

plt.figure(figsize=(10, 6))
plt.scatter(wine_df['Price'], wine_df['Rating'], alpha=0.5, color='blue')

plt.title('Scatter Plot of Price vs. Rating', fontsize=16)
plt.xlabel('Price (in USD)', fontsize=14)
plt.ylabel('Rating (out of 5)', fontsize=14)

plt.show()


# There seems to be more concentration of mid tier wines having stronger rating compared to more expensive wines
# The cluster is all uncer 100 hundred dollars. THe rest are a bit expensive but they are the same rating at hose under 100. Might come down to country
# or brand. 

# 
#                                 shows the average price and average rating of wines from each country
# import pandas as pd
# import matplotlib.pyplot as plt
# wine_df = pd.read_csv('datasets/White.csv')
# 
# https://dataplotplus.com/how-to-create-bar-plot-with-two-y-axis-bars-in-pandas/
# https://cmdlinetips.com/2019/10/how-to-make-a-plot-with-two-different-y-axis-in-python-with-matplotlib/#google_vignette
# https://www.statology.org/matplotlib-two-y-axes/

# country_avg = wine_df.groupby('Country').agg({'Price': 'mean', 'Rating': 'mean'}).reset_index()
# 
# 
# fig, ax1 = plt.subplots(figsize=(12, 6))
# ax1.bar(country_avg['Country'], country_avg['Price'], color='lightblue', alpha=0.7, label='Average Price ($$$)')
# ax1.set_xlabel('Country', fontsize=14)
# ax1.set_ylabel('Average Price ($$$)', fontsize=14, color='blue')
# ax1.set_title('Country Based Analysis: Average Price & Rating', fontsize=16)

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
wine_df = pd.read_csv('datasets/White.csv')

country_avg = wine_df.groupby('Country').agg({'Price': 'mean', 'Rating': 'mean'}).reset_index()
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(country_avg['Country'], country_avg['Price'], color='lightblue', alpha=0.7, label='Average Price ($$$)')
ax1.set_xlabel('Country', fontsize=14)
ax1.set_ylabel('Average Price ($$$)', fontsize=14, color='blue')
ax1.set_title('Country Based Analysis: Average Price & Rating', fontsize=16)


ax2 = ax1.twinx()
ax2.plot(country_avg['Country'], country_avg['Rating'], color='green', marker='o', label='Average Rating (out of 5)', linewidth=2)
ax2.set_ylabel('Average Rating (out of 5)', fontsize=14, color='green')

ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()


# France and Italy are looking good but considering those wines are well known around the world it is no surprise but other wines seem to
# be making waves. Spain apparently has something going well with it considering the rating. Lebanon wine is pretty high in the rating mark considering the wine it exports. In regards of price two countries stand out the most and I guess the wine reflects the quality. 

# In[ ]:




