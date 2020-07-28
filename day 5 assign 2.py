#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
print(list1)
print(list2)


# In[11]:



s1 = len(list1) 
s2 = len(list2) 
  
res = [] 
i, j = 0, 0
  
while i < s1 and j < s2: 
    if list1[i] < list2[j]: 
      res.append(list1[i]) 
      i += 1
  
    else: 
      res.append(list2[j]) 
      j += 1
  
res = res + list1[i:] + list2[j:] 
  

print ("The combined sorted list is : " + str(res)) 


# In[ ]:




