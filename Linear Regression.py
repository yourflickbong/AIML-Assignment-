#from sklearn.datasets import load_boston
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error

#housing = load_boston()
housing = fetch_california_housing()
housing.DESCR

data=pd.DataFrame(housing.data, columns=housing.feature_names)
data

data['MEDV']=pd.DataFrame(housing.target)
data


#find all correlation values, MedInc has highest with target MEDV
pd.DataFrame(data.corr().round(2))
#x=data['RM']
x=data['MedInc']
y=data['MEDV']

#Linear Regression
linearRegressionClassifier = LinearRegression()
x=pd.DataFrame(x)
y=pd.DataFrame(y)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
print(x_train.shape)
linearRegressionClassifier.fit(x_train, y_train)
y_pred=linearRegressionClassifier.predict(x_test)
y_pred.shape
np.sqrt(mean_squared_error(y_test, y_pred))
linearRegressionClassifier.score(x_test,y_test)