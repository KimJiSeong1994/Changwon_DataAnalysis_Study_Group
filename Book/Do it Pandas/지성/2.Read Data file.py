# =================================================== [ setting ] ==================================================
## + [ Data sorting ] ========
import pandas as pd
from dfply import *
import matplotlib.pyplot as plt

df = pd.read_csv("./Data/gapminder.tsv", sep = "\t")
# print(df.info()) # 각 values에 대한 정보 확인

contry_df = df[["country", "continent"]]
# df >>\
#     select(X.country, X.continent)

print(df.loc[:, ["year", "pop"]])
print(df.groupby("year")["lifeExp"].mean())
# df >>\
#     group_by(X.year) >>\
#     summarize(lefeExp = X.lifeExp.mean())

print(df.groupby(["year", "continent"])[["lifeExp", "gdpPercap"]].mean())
# print(df >>\
#     group_by(X.year, X.continent) >>\
#     summarize(lifeExp = X.lifeExp.mean(),
#               gdpPercap = X.gdpPercap.mean()))

print(df.groupby("continent")["country"].nunique())
# print(df >>\
#     group_by(X.continent) >>\
#     summarize(country = n(X.country)))

