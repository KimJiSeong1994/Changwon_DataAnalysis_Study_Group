# =================================================== [ setting ] ====================================================
import pandas as pd
import matplotlib.pyplot as plt

feature_name_df = pd.read_csv("./data/UCI HAR Dataset/features.txt", sep = "\s+", header = None, names = ["column_index", "columns_name"])
feature_name = feature_name_df.iloc[: 1].values.tolist()

feature_dup_df = feature_name_df.groupby("columns_name").count()
# print(feature_dup_df[feature_dup_df["column_index"] > 1].head())

def get_new_feature_name_df(old_feature_name_df) :
    feature_dup_df = pd.DataFrame(data = old_feature_name_df.groupby("column_name").cumcount(), columns = ["dup_cnt"])
    feature_dup_df = feature_dup_df.reset_index()

    new_feature_name_df = pd.merge(old_feature_name_df.reset_index(), feature_dup_df, how = "outer")
    new_feature_name_df["column_name"] = new_feature_name_df[["column_name", "dup_cnt"]].apply(lambda x : x[0] + "_" + str(x[1]) if x[1] > 0 else x[0], axis = 1)
    new_feature_name_df = new_feature_name_df.drop(["index"], axis = 1)
    return new_feature_name_df

def get_human_dataset() :
    feature_name_df = pd.read_csv("./data/UCI HAR Dataset/features.txt", sep = "\s+", header = None, names = ["columns_index", "column_name"])
    new_feature_name_df = get_new_feature_name_df(feature_name_df)
    feature_name = new_feature_name_df.iloc[:, 1].values.tolist()

    X_train = pd.read_csv("./data/UCI HAR Dataset/train/X_train.txt", sep = "\s+", names = feature_name)
    X_test = pd.read_csv("./data/UCI HAR Dataset/test/X_test.txt", sep = "\s+", names = feature_name)
    y_train = pd.read_csv("./data/UCI HAR Dataset/train/y_train.txt", sep = "\s+", header = None, names = ["action"])
    y_test = pd.read_csv("./data/UCI HAR Dataset/test/y_test.txt", sep = "\s+", header = None, names = ["action"])

    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = get_human_dataset()

# =================================================== [ modeling ] ====================================================
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import seaborn as sns

dt_clf = DecisionTreeClassifier(random_state = 2109)
dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
accuracy = accuracy_score(y_test, pred)
print("DecistionTreeClassifier Accuracy : {0:.4f}".format(accuracy)) # Accuracy : 0.8605

params = {"max_depth" : [6, 8, 10, 12, 16, 20, 24]}
grid_cv = GridSearchCV(dt_clf, param_grid = params, scoring = "accuracy", cv = 5)
grid_cv.fit(X_train, y_train)

print("GridSearchCV max mean_accuracy : {0:.4f}".format(grid_cv.best_score_))
print("GridSearchCV best parameter : ", grid_cv.best_params_)
cv_result_df = pd.DataFrame(grid_cv.cv_results_)
print(cv_result_df)

params = {"max_depth" : [8, 12, 16, 20],
          "min_sample_split" : [16, 24],}

grid_cv = GridSearchCV(dt_clf, param_grid = params, scoring = "accuracy", cv = 5)
grid_cv.fit(X_train, y_train)
print("GridSearchCV max mean_accuracy : {0:.4f}".format(grid_cv.best_score_))
print("GridSearchCV best parameter : ", grid_cv.best_params_)

best_df_clf = grid_cv.best_estimator_
pred1 = best_df_clf.predict(X_test)
accuracy = accuracy_score(y_test, pred1)
print("Best Decistiontree Classifier Accuracy : {0:.4f}".format(accuracy))

ftr_importances_values = best_df_clf.feature_importances_
ftr_importances = pd.Series(ftr_importances_values, index = X_train.columns)
ftr_top20 = ftr_importances.sort_values(asending = False)[:20]
plt.figure(figsize = (8, 6))
plt.title("Feature importances Top 20")
sns.barplot(x = ftr_top20, y = ftr_top20.index)
plt.show()