#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                    'Rank':[121,40,100,130,11]})
data


# In[3]:


#quick analysis of any data set using:
data.describe()


# In[4]:


data.sort_values(by=['Rank'],ascending=True,inplace=False)


# In[ ]:




