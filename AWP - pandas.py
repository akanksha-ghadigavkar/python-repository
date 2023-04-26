#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pandas
import pandas as pd
import numpy as np
Furniture={'Item':['Sofa','Dining Table','Chair','Sofa','Chair','Dining table'],
      'Material':['wooden','plywood','plastic','Stailess steel','wooden','aluminium'],
      'Colour':['Maroon','Yellow','Red','Silver','Light Blue','Golden'],
      'price':['25000','20000','1500','55000','2500','65000']}


# In[3]:


df=pd.DataFrame(Furniture)


# In[4]:


df


# In[5]:


#a) Display the details of the chair and sofa.
df.iloc [[0,2,3,4], : ]


# In[9]:


#indexing and slicing 
df["Material"]


# In[12]:


df[["Material","price"]]


# In[13]:


df.iloc[:]


# In[14]:


df.iloc[:2]


# In[16]:


df.iloc[:2,:3]


# In[17]:


df.iloc[1:3]


# In[19]:


df.iloc[3:-1]


# In[21]:


df.iloc[4,2]


# In[23]:


df.iloc[:,1]


# In[ ]:




