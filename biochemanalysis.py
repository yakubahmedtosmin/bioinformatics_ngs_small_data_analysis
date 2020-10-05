#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df1 = pd.read_csv("sequencing_data_biochem1.csv")
df2 = pd.read_csv("sequencing_data_biochem2.csv")


# In[3]:


df1.head()


# In[4]:


df2.head()


# In[5]:


print("details about the data set biochem1: ",df1.info())
print("details about the data set biochem2: ",df2.info())


# ## ** function to call the data frame and each cycles **
# ## ** the call function is to call the data and find the maximum value for each column, then make the call_2 column for format call_2 data in a represetable way**
# ## ** here i also seen that rows with '0' call in call_1 as N so for in cycle 2, for mimic the same
# 
# ## ## the function call_imp is a improvement function, where i drop the 0 valued rows for improve the accuracy of the experiment. 
# ## !! the error_rate function is to calculate the error of the data frame to validate it with the given one

# In[6]:


def call(df,x):
    x = str(x)
    df['call_' + x] = df.loc[:,['A_' + x, 'T_' + x, 'C_' + x, 'G_' + x]].idxmax(axis = 1)
    df['call_' + x] = df['call_' + x].str.replace("_" + x,"")
    df['call_' + x][df.loc[:,['A_' + x, 'T_' + x, 'C_' + x, 'G_' + x]].eq(0).all(1)] = "N"
    
def call_imp(df,x):
    x = str(x)
    df['call_' + x] = df.loc[:,['A_' + x, 'T_' + x, 'C_' + x, 'G_' + x]].idxmax(axis = 1)
    df['call_' + x] = df['call_' + x].str.replace("_" + x,"")
    list_ = list(df['call_' + x][df.loc[:,['A_' + x, 'T_' + x, 'C_' + x, 'G_' + x]].eq(0).all(1)].index)
    processed_df =  df.drop(list_)
    
    return error_rate(processed_df,x)
    
def error_rate(df,x):
    x = str(x)
    return (1 - (sum(df["call_" + x] == df["ref_" + x])/len(df)))* 100


# In[7]:


call(df1,2)


# In[8]:


df1.head() ##call for the second cycle in the biochem1 shown in call_2


# In[9]:


error_rate(df1,2) ## error rate before using the call_improve


# In[10]:


error_rate(df1,1) ## validate with given value to confirm the function woking


# In[11]:


call_imp(df1,2)  ## error rate after using improve function seen the rate is increase


# In[12]:


df2 = pd.read_csv("sequencing_data_biochem2.csv") # load the biochem2


# In[13]:


call(df2,1)


# In[14]:


call(df2,2)


# In[15]:


df2.head()


# # in the above output, i can see that the call is not related to ref in the both of the call. i can also infer that, say in the 1st row it should be G_1 in place of C_1. So, using this logic i will try to find out the, how many mispalce is happned. 
# 
# # all this work will be done below

# In[16]:


#call__1 = df2.call_1


# In[17]:


#call__1 = call__1.str.replace("_1", "")


# In[18]:


df2.call_1.loc[df2.ref_1 == "G"].value_counts() # this the no of C wher it should be G.


# In[19]:


df2.call_1.loc[df2.ref_1 == "T"].value_counts() # same logic for G to T


# In[20]:


df2.call_1.loc[df2.ref_1 == "C"].value_counts() # A to C


# In[21]:


df2.call_1.loc[df2.ref_1 == "A"].value_counts() # T to A


# In[22]:


df2.rename(columns = {'A_1':'C_1', 'C_1' : 'G_1', 'G_1' : 'T_1', "T_1" : "A_1"}, inplace = True)  # now i change the column name for first cycle. 


# In[23]:


df2.head()


# In[24]:


call(df2,1)


# In[25]:


df2.head() # after correcting the image capturing problem. I can see that in the 1st cycle its work properely. now I will do the same steps in the cycle 2.   


# In[26]:


df2.call_2.loc[df2.ref_2 == "G"].value_counts() # verify the same mistake and found the capture proprocessing is not working.


# In[27]:


df2.call_2.loc[df2.ref_2 == "T"].value_counts()


# In[28]:


df2.call_2.loc[df2.ref_2 == "C"].value_counts()


# In[29]:


df2.call_2.loc[df2.ref_2 == "A"].value_counts()


# In[30]:


df2.rename(columns = {'A_2':'C_2', 'C_2' : 'G_2', 'G_2' : 'T_2', "T_2" : "A_2"}, inplace = True) # now i change the column name for second cycle. 


# In[31]:


df2.head()


# # in the above data frame it is seen that the misprogramming is fixed.
# # now I will move for the error_rate calculation .

# In[32]:


error_rate(df2,1)


# In[33]:


call_imp(df2,1) # error rate is decreased.


# In[34]:


error_rate(df2,2)


# In[42]:


call_imp(df2,2) # error rate is decreased.


# In[ ]:


#verify the both datasets with output 


# In[43]:


df1.head()


# In[44]:


df2.head()


# # from this exercise i can infer that, the dye combination which they are using in the biochem1 cycle 1 is acceptable. they can use it for the other cycles, and if the image capturing mechanism is modified or corrected than they can use the previous dye combination to sequence the DNA.
