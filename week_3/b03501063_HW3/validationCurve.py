
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression 
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
def PolynomialRegression(degree=2, **kwargs): return make_pipeline(PolynomialFeatures(degree),
                       LinearRegression(**kwargs))


# In[2]:


def make_wave(n_samples=100):
      rnd = np.random.RandomState(42)
      x = rnd.uniform(-3, 3, size=n_samples)
      y_no_noise = (np.sin(4 * x) + x)
      y = (y_no_noise + rnd.normal(size=len(x))) / 2
      return x.reshape(-1, 1), y
X, y = make_wave(60)


# In[3]:


plt.scatter(X, y)


# In[4]:


X_test = np.linspace(-3, 3, 60)[:, None]
plt.scatter(X.ravel(), y, color='black')
for degree in [2, 3, 7]:
    y_test = PolynomialRegression(degree).fit(X, y).predict(X_test)
    plt.plot(X_test.ravel(), y_test, label='degree={0}'.format(degree))
plt.legend(loc='best')


# In[5]:


from sklearn.model_selection import validation_curve
degree = np.arange(0, 25)
train_score, val_score = validation_curve(PolynomialRegression(), X, y,
                                          'polynomialfeatures__degree', degree, cv=3)

plt.plot(degree, np.median(train_score, 1), color='blue', label='training score')
plt.plot(degree, np.median(val_score, 1), color='red', label='validation score')
plt.legend(loc='best')
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score')
plt.title('validation curves with 3-fold cross validadtion')


# In[6]:


from sklearn.model_selection import validation_curve
degree = np.arange(0, 25)
train_score, val_score = validation_curve(PolynomialRegression(), X, y,
                                          'polynomialfeatures__degree', degree, cv=7)

plt.plot(degree, np.median(train_score, 1), color='blue', label='training score')
plt.plot(degree, np.median(val_score, 1), color='red', label='validation score')
plt.legend(loc='best')
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score')
plt.title('validation curves with 7-fold cross validadtion')

