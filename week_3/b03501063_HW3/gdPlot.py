
# coding: utf-8

# In[1]:


from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


model = LinearRegression(fit_intercept=True)


# In[3]:


x = np.append(np.random.rand(2) +  -np.random.rand(2), 0)
y = np.sin(np.pi * x)
x


# In[4]:


X = x[:, np.newaxis]


# In[5]:


model.fit(X, y)


# In[6]:


a = model.coef_


# In[7]:


xfit = np.linspace(-1, 1)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)


# In[8]:


plt.title("a = %1.2f" %a)
plt.plot(xfit, np.sin(np.pi * xfit), '--', color = 'black', label = 'target')
plt.scatter(x[:2], y[:2])
plt.plot(xfit, yfit, color = 'black', label = 'best fit')
plt.legend()

