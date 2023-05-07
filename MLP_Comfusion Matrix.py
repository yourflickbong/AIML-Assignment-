from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import numpy as np

cancer_dataset = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer_dataset.data,cancer_dataset.target,test_size=0.25)

classifier = MLPClassifier(hidden_layer_sizes=(150,100,50), max_iter=300,activation = 'relu',solver='adam',random_state=1)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
cf_matrix = confusion_matrix(y_test, y_pred)
print(cf_matrix)

cf_matrix=np.transpose(np.transpose(cf_matrix) / cf_matrix.astype(float).sum(axis=1))
cf_matrix