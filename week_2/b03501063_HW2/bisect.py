
# coding: utf-8

# In[174]:


def f(x) :
    return 2*x - 3


# In[183]:


def bisection(f, a, b, eps) :
    n = 0
    while ((b - a >= eps) and (f(a) * f(b) <= 0)) : 
        m = (a+b) / 2
        if (f(a) * f(m) > 0) :
            a = m
        else :
            b = m
        n = n + 1
        print("Interation:", n, "interval =", [a, b])
    print("The root is", a, "found in", n, "iterations")    
    return (a, b)


# In[184]:


bisection(f, 0, 3, eps = 1E-5)


# In[185]:


import math
def g(x) :
    return x-(x-1)*math.sin(x)


# In[186]:


bisection(g, -2, 1, eps = 1E-6)

