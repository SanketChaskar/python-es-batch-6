#!/usr/bin/env python
# coding: utf-8

# In[7]:


list1=[1,2,3,4,5,7,8]
list2=["a","b","c","d","e"]
print(list1)
print(list2)


# In[8]:


print ("Original key list is : " + str(list1)) 
print ("Original value list is : " + str(list2)) 
  
res = dict(zip(list1, list2)) 
  

print ("Resultant dictionary is : " +  str(res)) 


# In[ ]:




