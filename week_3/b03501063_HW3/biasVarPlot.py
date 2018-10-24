
# coding: utf-8

# In[6]:


from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


model = LinearRegression(fit_intercept=True)


# In[8]:


a_sum = 0
ic_sum = 0
for i in range(0,100000):
    x = np.append(np.random.rand(2) +  -np.random.rand(2),0)
    y = np.sin(np.pi * x)
    X = x[:, np.newaxis]
    model.fit(X, y)
    xfit = np.linspace(-1, 1)
    Xfit = xfit[:, np.newaxis]
    yfit = model.predict(Xfit)
    a = model.coef_
    ic = model.intercept_
    a_sum = a_sum + a 
    ic_sum = ic_sum + ic
a_bar = a_sum / 100
ic_bar = ic_sum / 100


# In[9]:


x_train = np.append(np.random.rand(2) +  -np.random.rand(2),0)
X_train = x_train[:, np.newaxis]
y_train =  y = np.sin(np.pi * x_train)
model.fit(X_train, y)
a = model.coef_
ic = model.intercept_
xfit = np.linspace(-1, 1)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)


# In[10]:


bias = abs((a_bar * xfit + ic_bar) - (np.sin(np.pi * xfit)))
var =  abs((a * xfit + ic) - (a_bar * xfit + ic_bar))
plt.plot(xfit, bias, '--', label = "bias(x)")
plt.plot(xfit, var, label = "var(x)")
plt.title("abar = %1.2f" %a_bar)
plt.legend()

