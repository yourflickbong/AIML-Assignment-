from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits = load_digits()
x_train, x_test, y_train, y_test=train_test_split(digits.data,digits.target,test_size=0.25)
dt2=DecisionTreeClassifier(criterion="entropy")
dt2.fit(x_train, y_train)

dt2.score(x_test,y_test)

dt3=DecisionTreeClassifier(max_depth=30)
dt3.fit(x_train, y_train)

dt3.score(x_test,y_test)