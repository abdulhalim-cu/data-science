
# coding: utf-8

# # 4. Why do some pandas commands end with parentheses (and others don't)

# In[1]:

import pandas as pd


# In[2]:

movies = pd.read_csv('http://bit.ly/imdbratings')


# In[3]:

movies.head()


# In[4]:

movies.describe()


# In[6]:

movies.shape


# In[9]:

# data type of six columns
movies.dtypes


# In[11]:

movies.describe(include=['object'])


# In[ ]:



