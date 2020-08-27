# ==================================================== [ setting ] ====================================================
import pandas as pd
from dfply import *
s = pd.Series(["Wes Mckinnery", "Creator of Pandas"], index = ["person", "Who"]) # Series type 만들기
# print(s)

scientists = pd.DataFrame({"name" : ["Rosaline Franklin", "William Gosset"],
                           "Occupation" : ["Chemist", "Statistician"],
                           "Born" : ["1920--7-25", "1876-06-13"],
                           "Died" : ["1958-04-16", "1937-10-16"],
                           "Age" : [37, 61]},
                          index = ["Rosaline Franklin", "William Gosset"],
                          columns = ["Occupation", "Born", "Age", "Died"]) # Dataframe 만들기
# print(scientists)

from collections import OrderedDict
scientists = pd.DataFrame(OrderedDict([
    ("Name", ["Rosaline Franklin", "william Gosset"]),
    ("Occupation", ["Chemist", "Statistician"]),
    ("Born", ["1920-07-25", "1876-06-13"]),
    ("Died", ["1958-04-16", "1937-10-16"]),
    ("Age", [37, 61])])) # 딕셔너리 입력의 순서를 유지
# print(scientists)

scientists = pd.read_csv("./Data/scientists.csv")
# print(scientists["Age"].max())
# print(scientists["Age"].mean())
# print(scientists[scientists["Age"] > scientists["Age"].mean()])
# print(scientists["Age"].sort_index(ascending = False))
# print(scientists[scientists["Age"] > scientists["Age"].mean()])
# print(scientists.info())

scientists["Born"] = pd.to_datetime(scientists["Born"], format = "%Y-%m-%d") # make date-type value
scientists["Died"] = pd.to_datetime(scientists["Died"], format = "%Y-%m-%d")
scientists["Age_days_dt"] = (scientists["Died"] - scientists["Born"]) # 날자 계산
# print(scientists)

scientists = scientists.drop(["Age"], axis = 1) # 변수 탈락
# print(scientists)

