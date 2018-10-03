
# coding: utf-8

# In[7]:


import math


# In[29]:


def sin_approx(x):
    N = 1
    sum = 0
    while (N <= 25):
        sin_x = pow(x, 2*N -1) / math.factorial(2*N - 1) * pow(-1, N-1)
        sum += sin_x
        N = N + 1
    return sum


# In[33]:


print("sin(1.2) approximation is", sin_approx(1.2))

