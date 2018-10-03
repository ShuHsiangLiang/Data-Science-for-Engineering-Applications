
# coding: utf-8

# In[48]:


import sun_data as sun
import numpy as np
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# In[51]:


ave_month = np.zeros(12)
for i in sun.data:
    for j in range(0, 12):
        ave_month[j] = ave_month[j] + i[j]
        
for i in range(0, 12):
    print(month[i], ave_month[i] / len(sun.data))

