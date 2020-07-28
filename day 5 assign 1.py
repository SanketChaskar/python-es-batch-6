#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('sort in increasing order but all zeros at right hand side')


# In[4]:


list=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
print(list)


# In[6]:


dir(list)


# In[9]:


help(sorted)


# In[10]:


sorted(list)


# In[12]:


list=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
temp=[]
for i in list:
   if int(i)==0:
       temp.append(i)
       list.remove(i)
for i in range(len(temp)):
    list.append(temp[i])
print(list)


# In[ ]:




