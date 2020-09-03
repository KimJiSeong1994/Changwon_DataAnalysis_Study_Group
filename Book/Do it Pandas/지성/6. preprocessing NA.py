# ==================================================== [ setting ] ===============================================
import pandas as pd
import numpy as np

ebola = pd.read_csv("./Data/country_timeseries.csv")
num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)

# print(np.count_nonzero(ebola.isunll()))
# print(np.count_nonzero(ebola["Cases_Guinea"].isnull()))
# print(ebola.Cases_Guinea.value_counts(dropna = False).head())
ebola.apply(lambda x : sum(ebola.isna()) / ebola.shape[0] * 100) # NA_prob

print(ebola.fillna(0).iloc[0:10, 0:5])
print(ebola.fillna(method = "ffill").iloc[0:10, 0:5]) # ffill = 변경전인 원래의 "NA" 값으로 되돌림
print(ebola.fillna(method = "bfill").iloc[0:10, 0:5])
print(ebola.interpolate().iloc[0:10, 0:5])
print(ebola.dropna())

ebola["Cases_multiple"] = ebola["Case_Guinea"] + ebola["Cases_Liberia"] + ebola["Cases_SierraLeone"]
print(ebola.Cases_Guinea.sum(skipna = True)) # NA값은 계산 x


