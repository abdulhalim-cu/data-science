
# coding: utf-8

# In[1]:

import pandas as pd


# In[12]:

ufo = pd.read_csv('http://bit.ly/uforeports')


# In[13]:

type(ufo)


# In[14]:

ufo.head()


# In[19]:

type(ufo['City'])


# In[20]:

ufo['City'].head()


# In[23]:

ufo.City.head() # sane as ufo['City'].head()


# In[26]:

ufo['Colors Reported'].head() # cannot use 'ufo.Color Reported'


# In[29]:

type(ufo.shape)


# In[30]:

ufo.shape[0] # returns total rows


# In[32]:

ufo.shape[1] # returns total columns


# In[34]:

city_state = ufo.City + '[' + ufo.State + ']'


# In[35]:

city_state.head()


# In[41]:

# create a new series names location
# should use bracket notation to create a series
ufo['Location'] = ufo.City + ', ' + ufo.State


# In[42]:

ufo.head()


# In[ ]:




# In[ ]:



