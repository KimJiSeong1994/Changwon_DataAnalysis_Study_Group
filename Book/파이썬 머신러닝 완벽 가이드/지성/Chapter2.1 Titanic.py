# ==================================================== [ setting ] ====================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def preprocess(df) :
    ## + todo [ replace NA ] ===================
    df["Age"].fillna(df["Age"].mean(), inplace = True)
    df["Cabin"].fillna("M", inplace = True)
    df["Embarked"].fillna("N", inplace = True)
    df["Fare"].fillna(0, inplace = True)

    ## + todo [ remove columns ] ===============
    df.drop(["PassengerId", "Name", "Ticket"], axis = 1, inplace = True)

    ## + todo [ Label encoding ] ===============
    df["Cabin"] = df["Cabin"].str[:1]
    features = ["Cabin", "Sex", "Embarked"]
    for features in features :
        le = preprocessing.LabelEncoder()
        le = le.fit(df[features])
        df[features] = le.transform(df[features])

    return df

train_df =  preprocess(pd.read_csv("./data/train.csv", encoding = "utf-8"))
label_df = train_df["Survived"]
train_df.drop("Survived", axis = 1, inplace = True)

# ==================================================== [ modeling ] ====================================================
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold


def exec_kfold(clf, folds = 5) :
    kfold = StratifiedKFold(n_splits = folds)
    scores = []

    for iter_count, (train_index, test_index) in enumerate(kfold.split(train_df, label_df)) :
        X_train, X_test = train_df.values[train_index], train_df.values[test_index]
        y_train, y_test = label_df.values[train_index], label_df.values[test_index]

        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        scores.append(accuracy)
        print("Crossvalidation {0} accuracy : {1:.4f}".format(iter_count, accuracy))

    mean_score = np.mean(scores)
    print("mean accuracy : {0:.4f}".format(mean_score))

dt_clf = DecisionTreeClassifier(random_state=2109)
exec_kfold(dt_clf, folds = 5)
