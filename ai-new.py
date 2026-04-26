# Check the versions of libraries

# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
# Load libraries
import pandas

import seaborn as sns

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
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
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

# Load dataset
url = "C:/Users/3019/machinelearning/iris.csv"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train,X_test,y_train,y_test = train_test_split(X,Y)

# Make predictions on validation dataset
knn = KNeighborsRegressor(n_neighbors=7)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
np.sqrt(mean_squared_error(y_test,y_pred))


#predict using SVC


svc = SVC(gamma='auto')
svc.fit(X_train,y_train)
y_pred2 = svc.predict(X_test)
np.sqrt(mean_squared_error(y_test,y_pred2))
