# ================================================= [ setting ] =======================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def get_outlier(df = None, column = None, weight = 1.5) :
    fraud = df[df["Class"] == 1][column]
    quantile_25 = np.percentile(fraud.values, 25)
    quantile_75 = np.percentile(fraud.values, 75)
    iqr_weight = (quantile_75 - quantile_25) * weight
    lowest_val = quantile_25 - iqr_weight
    highest_val = quantile_75 + iqr_weight
    outlier_index = fraud[(fraud < lowest_val) | (fraud > highest_val)].index

    return outlier_index

def get_train_test_dataset(file_path) :
    df = pd.read_csv(file_path)

    amount_n = np.log1p(df["Amount"])
    df.insert(0, "Amount_scaled", amount_n)
    df.drop(["Time", "Amount"], axis=1, inplace = True)

    outlier_index = get_outlier(df = df, column = "V14", weight = 1.5)
    df.drop(outlier_index, axis = 0, inplace = True)

    X_features = df.iloc[:, :-1]
    y_target = df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X_features, y_target, test_size = 0.3, random_state = 2109, stratify = y_target)

    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = get_train_test_dataset("./data/Credit_card_Fraud_Detection/creditcard.csv")

# ================================================ [ modeling ] =======================================================
## + [ LogisticRegression ] =======
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, precision_recall_curve
from sklearn.metrics import f1_score, confusion_matrix, precision_score, roc_curve

lr_clf = LogisticRegression()
lr_clf.fit(X_train, y_train)
lr_pred = lr_clf.predict(X_test)
lr_pred_proba = lr_clf.predict_proba(X_test)[:, 1]

def get_clf_eval(y_test, pred = None, pred_proba = None) :
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    roc_auc = roc_auc_score(y_test, pred_proba)
    print("confusion matrix")
    print(confusion)
    print("accuacy : {0:.4F}, precison : {1:.4f}, recall : {2:.4f}, F1-score : {3:.4f}, ROC_AUC : {4:.4f}".format(accuracy, precision, recall, f1, roc_auc))

get_clf_eval(y_test, lr_pred, lr_pred_proba)

## + [ LightGBM ] ==========
from lightgbm import LGBMClassifier

def get_model_train_eval(model, ftr_train = None, ftr_test = None, tgt_train = None, tgt_test = None) :
    model.fit(ftr_train, tgt_train)
    pred = model.predict(ftr_test)
    pred_proba = model.predict_proba(ftr_test)[:, 1]
    get_clf_eval(tgt_test, pred, pred_proba)

lgbm_clf = LGBMClassifier(n_estimators = 1000, num_leaves = 64, n_jobs = -1, boost_from_average = False)
get_model_train_eval(lgbm_clf, ftr_train = X_train, ftr_test = X_test, tgt_train = y_train, tgt_test = y_test)

# ============================================= [ SMOTE over sampling ] ================================================
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state = 2109)
X_train_over, y_train_over = smote.fit_sample(X_train, y_train)

lr_clf = LogisticRegression()
get_model_train_eval(lr_clf, ftr_train = X_train_over, ftr_test = X_test, tgt_train = y_train_over, tgt_test = y_test)

lgbm_clf = LGBMClassifier(n_estimators = 1000, num_leaves = 64, n_jobs = -1, boost_from_average = False)
get_model_train_eval(lgbm_clf, ftr_train = X_train_over, ftr_test = X_test, tgt_train = y_train_over, tgt_test = y_test)
