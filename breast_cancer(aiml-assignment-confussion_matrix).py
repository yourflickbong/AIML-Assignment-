import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer_dataset = load_breast_cancer()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
cancer_dataset.data,cancer_dataset.target,test_size=0.25)


from sklearn.neural_network import MLPClassifier

classifier = MLPClassifier(hidden_layer_sizes=(150,100,50), max_iter=300,
activation = 'relu',solver='adam',random_state=1)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix

cf_matrix = confusion_matrix(y_test, y_pred)
print(cf_matrix)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

y_pred_log = log_reg.predict(X_test)

cf_matrix_log = confusion_matrix(y_test, y_pred_log)
print(cf_matrix_log)

print("TP:", cf_matrix_log[1][1])
print("TN:", cf_matrix_log[0][0])
print("FP:", cf_matrix_log[0][1])
print("FN:", cf_matrix_log[1][0])

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_pred_dtc = dtc.predict(X_test)

cf_matrix_dtc = confusion_matrix(y_test, y_pred_dtc)
print(cf_matrix_dtc)

print("TP:", cf_matrix_dtc[1][1])
print("TN:", cf_matrix_dtc[0][0])
print("FP:", cf_matrix_dtc[0][1])
print("FN:", cf_matrix_dtc[1][0])