
# coding: utf-8

# In[1]:


from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


model = LinearRegression(fit_intercept=True)


# In[3]:


a_sum = 0
for i in range(0,100):
    x = np.append(np.random.rand(2) +  -np.random.rand(2),0)
    y = np.sin(np.pi * x)
    X = x[:, np.newaxis]
    model.fit(X, y)
    xfit = np.linspace(-1, 1)
    Xfit = xfit[:, np.newaxis]
    yfit = model.predict(Xfit)
    a = model.coef_
    a_sum = a_sum + a 
    plt.plot(xfit, yfit, color = 'black')
    plt.scatter(x[:2], y[:2])
a_bar = a_sum / 100
plt.plot(xfit, np.sin(np.pi * xfit), color = 'red', label = 'target')
plt.legend()
plt.title("abar = %1.2f" %a_bar)

