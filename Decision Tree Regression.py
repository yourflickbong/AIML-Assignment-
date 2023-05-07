#from sklearn.datasets import load_boston
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor


#housing = load_boston()
housing = fetch_california_housing()
housing.DESCR

data=pd.DataFrame(housing.data, columns=housing.feature_names)
data

data['MEDV']=pd.DataFrame(housing.target)
data

pd.DataFrame(data.corr().round(2))

#x=data[['RM',''ZN]]
x=data[['MedInc','AveRooms']]
x

y=data['MEDV']
y

x=pd.DataFrame(x)
y=pd.DataFrame(y)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
y_train

#Decision Tree Regressor
dt1=DecisionTreeRegressor(max_depth=20)
dt1.fit(x_train,y_train)
y_pred1=dt1.predict(x_test)

np.sqrt(mean_squared_error(y_test, y_pred1))

rf1=RandomForestRegressor()
rf1.fit(x_train, y_train)

rf1.score(x_test,y_test)

y_pred2=rf1.predict(x_test)
np.sqrt(mean_squared_error(y_test, y_pred2))