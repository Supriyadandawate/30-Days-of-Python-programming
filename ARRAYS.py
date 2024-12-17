#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list_01 =[26,87,24,56]
np.array(list_01)


# In[2]:


#2-D Numpy array
import numpy as np 
list_02 = [[26,87,24,56],[15,67,45,98],[65,34,96,16]]
np.array(list_02)


# In[3]:


np.zeros((4,3))


# In[4]:


np.ones((3,2))


# In[5]:


np.linspace(2,26,10)


# In[6]:


np.arange(2,26,4)


# In[7]:


np.eye(4)


# In[8]:


matrix_1d = np.random.random(4)
matrix_2d = np.random.random((2,3))

print(matrix_1d)
print("-------------------------")
print("-------------------------")
print(matrix_2d)


# In[9]:


np.random.randint(4,67,15)


# In[10]:


array_01 = np.arange(30)
array_01.reshape(6,5)

