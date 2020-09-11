# ================================================== [ setting ] ==================================================
import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")
tips["sex_str"] = tips["sex"].astype(str)
tips["total_bill"] = tips["total_bill"].astype(str)
tips["total_bill"] = tips["total_bill"].astype(float)
# print(tips.dtypes)

tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], "total_bill"] = "missing"
# print(tips_sub_miss)

tips_sub_miss["total_bill"] = pd.to_numeric(tips_sub_miss["total_bill"], errors = "ignore")
tips_sub_miss["total_bill"] = pd.to_numeric(tips_sub_miss["total_bill"], errors = "coerce") # missing 값을 NaN
tips_sub_miss["total_bill"] = pd.to_numeric(tips_sub_miss["total_bill"], errors = "coerce", downcast = "float")

tips["sex"] = tips["sex"].astype("str")
tips["sex"] = tips["sex"].astype("category")
print(tips.info())