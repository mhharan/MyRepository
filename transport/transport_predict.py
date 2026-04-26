#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

#load in the data
df = pd.read_csv('C:/Users/3019/machinelearning/transport/Transport Analytics_DS for Python1.csv')



df_trans=pd.get_dummies(df)
X = df_trans.drop(['LINEAMOUNT'],axis=1)
y=df_trans['LINEAMOUNT']
features = X.columns


#scale the data
s = StandardScaler()
X = s.fit_transform(X)

#X_train,X_test,y_train,y_test = train_test_split(X,y)

#predict using KNN

knn = KNeighborsRegressor(n_neighbors=7)
knn.fit(X,y)


df['knn_prediction']=knn.predict(X)

df.to_csv('C:/Users/3019/machinelearning/transport/output.csv') 