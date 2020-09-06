# =============================================== [ setting ] =======================================================
import pandas as pd
from dfply import *

pew = pd.read_csv("./Data/pew.csv")
pew_long = pd.melt(pew, id_vars = "religion")
pew_long = pd.melt(pew, id_vars = "religion", var_name = "income", value_name = "count")
# print(pew >>\
#       gather("variable", "value", ["<$10k", "$10-20k", "$30-40k", "$40-50k"]) >>\
#       select(X.religion, X.variable, X.value))

billboard = pd.read_csv("./Data/billboard.csv")
billboard_long = pd.melt(billboard, id_vars = ["year", "artist", "track", "time", "date.entered"], var_name = "week", value_name = "rating")

ebola = pd.read_csv("./Data/country_timeseries.csv")
ebola_long = pd.melt(ebola, id_vars = ["Date", "Day"])
variable_split = ebola_long.variable.str.split("_")
status_values = variable_split.str.get(0)  # list 형태로 반환된 값을 출력 ex) ["질병종류", "나라"], str.get(0), str.get(1) 형태
country_values = variable_split.str.get(1)
ebola_long["status_values"] = status_values
ebola_long["country_values"] = country_values

# variable_split = ebola_long.variable.str.split("_", expand = True)
# variable_split.columns = ["status", "country"]
# ebola_parsed = pd.concat([ebola_long, variable_split], axis = 1)

weather = pd.read_csv("./Data/weather.csv")
weather_melt = pd.melt(weather, id_vars = ["id", "year", "month", "element"], var_name = "day", value_name = "temp")
weather_tidy = weather_melt.pivot_table(index = ["id", "year", "month", "day"],
                                        columns = "element",
                                        values = "temp",
                                        dropna = False)
weather_tidy_flat = weather_tidy.reset_index()

billboard_long = pd.melt(billboard, id_vars = ["year", "artist", "track", "time", "date.entered"], var_name = "week", value_name = "rating")
billboard_songs = billboard_long[["year", "artist", "track", "time"]].drop_duplicates()
billboard_songs["id"] = range(len(billboard_songs))
billboard_ratings = billboard_long.merge(billboard_songs, on = ["year", "artist", "track", "time"])

import os
import urllib.request
import glob

with open("./Data/raw_data_urls.txt", "r") as data_urls :
    for line, url in enumerate(data_urls) :
        if line == 5 :
            break
        fn = url.split("/")[-1].strip()
        fp = os.path.join("", "./Data", fn)
        print(url)
        print(fp)
        urllib.request.url2pathname(url, fp)

nyc_taxi_data = glob.glob("./Data/fhv_*")
print(nyc_taxi_data)

list_taxi_df = []
for csv_filename in nyc_taxi_data :
    df = pd.read_csv(csv_filename)
    list_taxi_df.append(df)
taxi_loop_concat = pd.concat(list_taxi_df)