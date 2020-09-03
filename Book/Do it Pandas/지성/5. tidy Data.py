# ============================================ [ setting ] =======================================================
import pandas as pd

df1 = pd.read_csv("./Data/concat_1.csv")
df2 = pd.read_csv("./Data/concat_2.csv")
df3 = pd.read_csv("./Data/concat_3.csv")

row_concat = pd.concat([df1, df2, df3]) # bind_row | rbind function in R

# new_row_series = pd.Series(["n1", "n2", "n3", "n4"])
# print(pd.concat([df1, new_row_series])) # X : Series type은 변수명을 가지지 않은 벡터 임으로

new_row_df = pd.DataFrame([["n1", "n2", "n3", "n4"]], columns = ["A", "B", "C", "D"])
print(pd.concat([df1, new_row_df]))

row_concat_i = pd.concat([df1, df2, df3], ignore_index = True) # row_number reset
col_concat = pd.concat([df1, df2, df3], axis = 1) # cbind | bind_col function in R
print(pd.concat([df1, df2, df3], axis = 1, ignore_index = True))

df1.columns = ["A", "B", "C", "D"]
df2.columns = ["E", "F", "G", "H"]
df3.columns = ["A", "C", "F", "H"]
print(pd.concat([df1, df2, df3], join = "inner")) # 공통된 칼럼만 붙이기

df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]
print(pd.concat([df1, df3], axis = 1, join = "inner"))

person = pd.read_csv("./Data/survey_person.csv")
site = pd.read_csv("./Data/survey_site.csv")
survey = pd.read_csv("./Data/survey_survey.csv")
visited = pd.read_csv("./Data/survey_visited.csv")
visited_subset = visited.loc[[0, 2, 6], ]

o2o_merge = site.merge(visited_subset, left_on = "name", right_on = "site")
print(o2o_merge)

m2o_merge = site.merge(visited, left_on = "name", right_on = "site")
print(m2o_merge)

ps = person.merge(survey, left_on = "ident", right_on = "person")
vs = visited.merge(survey, left_on = "ident", right_on = "taken")
ps_vs = ps.merge(vs, left_on = ["ident", "taken", "quant", "reading"], right_on = ["person", "ident", "quant", "reading"])
