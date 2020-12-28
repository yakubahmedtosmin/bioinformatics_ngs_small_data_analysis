#!/usr/bin/env python
# coding: utf-8

# In[1]:


def  round_of(df):
    for i in df.columns[1:]:
        x= df[i]
        df[i] = int((x-0.5)+1)


# In[2]:


import numpy as np
import pandas as pd
demomat = pd.read_csv("Demomatrix.xls", delimiter='\t')
demomat.head(20)


# In[3]:


round_of(demomat)


# In[4]:


demomat = demomat.round(0)


# In[5]:


demomat.head(20)


# In[6]:


demomat.to_csv("round_off.csv")


# In[ ]:




