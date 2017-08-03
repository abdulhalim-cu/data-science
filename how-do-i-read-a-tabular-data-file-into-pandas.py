
# coding: utf-8

# In[1]:

import pandas as pd


# In[5]:

orders = pd.read_table('http://bit.ly/chiporders')


# In[6]:

orders.head()


# In[16]:

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)


# In[17]:

users.head()


# In[ ]:



