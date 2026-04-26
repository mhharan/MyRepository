#!/usr/bin/env python
# Three models will be evaluated which is Standard Linear Regression, Random Forest Reggressor and K means Regressor.

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import  LinearRegression, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt


#load in the data
df = pd.read_csv('C:\\Users\\3019\\machinelearning\\pbiexample\\Transport Analytics_DS for Python1.csv')

df_trans=pd.get_dummies(df)
X = df_trans.drop(['LINEAMOUNT'],axis=1)
y=df_trans['LINEAMOUNT']
features = X.columns


#scale the data
s = StandardScaler()
X = s.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,y)


# # K-Neighbours Regressor

# In[20]:


knn = KNeighborsRegressor(n_neighbors=7)
knn.fit(X_train,y_train)


# In[21]:


y_pred = knn.predict(X_test)


df['prediction']=knn.predict(X)

df.to_csv('C:\\Users\\3019\\machinelearning\\pbiexample\\file1.csv') 