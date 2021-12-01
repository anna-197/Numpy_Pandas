#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x1 = np.array([4, 3, 4, 4, 8, 4])
x1


# In[2]:


x1[4]


# In[3]:


#get the second last value
x1[-2]


# In[7]:


x2 = np.random.randint(10, size=(3,4)) #two dimension
x2


# In[8]:


#3rd row and last value from the 3rd column
x2[2,-1]


# In[9]:


#replace value at 0,0 index
x2[0,0] = 12
x2

