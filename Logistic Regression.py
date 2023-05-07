from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

digits = load_digits()
digits.DESCR
digits.data
digits.data.shape
d = digits.data[0:500]
d.shape
digits.target.shape
image = digits.data[0]
image
digits.target[0]
np.reshape(image,(8,8))
plt.imshow(np.reshape(image,(8,8)),cmap='BuGn')
plt.show()

#Logistic Regression
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)
log_reg1= LogisticRegression(max_iter=100000)
log_reg1.fit(x_train, y_train)
y_pred=log_reg1.predict(x_test)
print(log_reg1.score(x_test,y_test))