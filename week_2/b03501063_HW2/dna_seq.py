
# coding: utf-8

# In[54]:


def gc_content(x) :
    num = 0
    i = 0
    for i in x :
        if (i == 'G' or i == 'C') :
            num = num + 1
    return num / len(x)


# In[55]:


seq50 = 'AACCTTGG'
gc_content(seq50)


# In[56]:


seq75 = 'ATCCCGGG'
gc_content(seq75)


# In[57]:


seq40 = 'ATATTTCGCG'
gc_content(seq40)

