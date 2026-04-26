#!/usr/bin/env python

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

from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils

#load in the data
#EmployeeID	EmployeeName	Department	Designation	Division	Location	TACategoryName	TotalPayableAmount	City	Days	PassedAmountInINR	StateID	TotalAmount	Hotel


df = pd.read_csv('C:/Users/3019/machinelearning/pbiexample/another/tabill.csv')

df_clean=df.drop(['City'],axis=1)
df_clean=df_clean.drop(['Hotel'],axis=1)
df_clean=df_clean.drop(['Department'],axis=1)
df_clean=df_clean.drop(['EmployeeID'],axis=1)
df_clean=df_clean.drop(['EmployeeName'],axis=1)
df_clean=df_clean.drop(['Designation'],axis=1)
df_clean=df_clean.drop(['Division'],axis=1)
df_clean=df_clean.drop(['Location'],axis=1)
df_clean=df_clean.drop(['TotalPayableAmount'],axis=1)
df_clean=df_clean.drop(['PassedAmountInINR'],axis=1)

df_trans=pd.get_dummies(df_clean)
X = df_trans.drop(['TotalAmount'],axis=1)
y=df_trans['TotalAmount']
features = X.columns


#scale the data
s = StandardScaler()
X = s.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,y)

#predict using KNN

knn = KNeighborsRegressor(n_neighbors=7)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)


df['knn_prediction']=knn.predict(X)

df.to_csv('C:/Users/3019/machinelearning/pbiexample/another/tabill_output.csv') 