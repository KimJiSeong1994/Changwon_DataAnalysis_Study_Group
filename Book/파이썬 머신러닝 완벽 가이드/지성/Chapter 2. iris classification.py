# ==================================================== [ setting ] ===================================================
import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, StratifiedKFold, GridSearchCV
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

iris = load_iris()
iris_data = iris.data
iris_label = iris.target
iris_df = pd.DataFrame(iris_data, columns = iris.feature_names)
iris_df["label"] = iris_label

# ==================================================== [ modeling ] ===================================================
## + [ DecisionTree model ] ==========
# dt_clf = DecisionTreeClassifier(random_state = 2109)
#
# kfold = StratifiedKFold(n_splits = 5)
# cv_accuracy =  []
# n_iter = 0
#
# for train_index, test_index in kfold.split(iris_data, iris_label) :
#     X_train, X_test = iris_data[train_index], iris_data[test_index]
#     y_train, y_test = iris_label[train_index], iris_label[test_index]
#
#     dt_clf.fit(X_train, y_train)
#     pred = dt_clf.predict(X_test)
#     n_iter += 1
#     accuracy = np.round(accuracy_score(y_test, pred), 4)
#     print("\n#{0} CrossValidation Accuracy : {1}".format(n_iter, accuracy))
#
#     cv_accuracy.append(accuracy)
#
# print("\n## mean Test Accuracy : ", np.mean(cv_accuracy))

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.2, random_state = 2109)
dtree = DecisionTreeClassifier()
parametres = {"max_depth" : [1, 2, 3],
              "min_samples_split" : [2 ,3]}

grid_dtree = GridSearchCV(dtree, param_grid = parametres, cv = 5, refit = True)
grid_dtree.fit(X_train, y_train)
print("GridSearchCV Best Parametres : ", grid_dtree.best_params_)
print("GridSearchCV Best Score : ", grid_dtree.best_score_)

estimator = grid_dtree.best_estimator_
pred = estimator.predict(X_test)
print("Test Dataset Accuracy : {0: .4f}".format(accuracy_score(y_test, pred)))