# ============================================== [ setting ] ====================================================
import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")

# ============================================== [ plotting ] ====================================================
# + [ 4.1 ] ===================
# dataset_1 = anscombe[anscombe["dataset"] == "I"]
# plt.plot(dataset_1["x"], dataset_1["y"])
# plt.show()
# plt.plot(dataset_1["x"], dataset_1["y"], "o") # `o` : scatter plot
# plt.show()

dataset_1 = anscombe[anscombe["dataset"] == "I"]
dataset_2 = anscombe[anscombe["dataset"] == "II"]
dataset_3 = anscombe[anscombe["dataset"] == "III"]
dataset_4 = anscombe[anscombe["dataset"] == "IV"]

# setting figure siae
fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

# setting subplot scatter plot
axes1.plot(dataset_1["x"], dataset_1["y"], "o")
axes2.plot(dataset_2["x"], dataset_2["y"], "o")
axes3.plot(dataset_3["x"], dataset_3["y"], "o")
axes4.plot(dataset_4["x"], dataset_4["y"], "o")

# setting subplot title
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

fig.suptitle("Anscombe Data") # setting title
fig.tight_layout()
plt.show()

# + [ 4.2 ] ===================
tips = sns.load_dataset("tips")
# print(tips.head())

fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips["total_bill"], bins = 10)
axes1.set_title("Histogram of Total Bill")
axes1.set_xlabel("Frequency")
axes1.set_ylabel("Total Bill")
plt.show()

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips["total_bill"], tips["tip"])
axes1.set_title("Scatterplot of Total Bill vs. Tip")
axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")
plt.show()

boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)
axes1.boxplot([tips[tips["sex"] == "Female"]["tip"],
               tips[tips["sex"] == "Male"]["tip"]],
              labels = ["Female", "Male"])
axes1.set_xlabel("Sex")
axes1.set_ylabel("Tip")
axes1.set_title("Boxplot of Tips by Sex")
plt.show()

def recode_sex(sex) :
    if sex == "Female" :
        return 0
    else :
        return 1

tips["sex_color"] = tips["sex"].apply(recode_sex)
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(x = tips["total_bill"],
              y = tips["tip"],
              s = tips["size"] * 10,
              c = tips["sex_color"],
              alpha = 0.5)
axes1.set_title("Total Bvill vs. Tip Colored by Sex and Sized by Size")
axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")
plt.show()

# + [ 4.3 ] ===================
ax = plt.subplot()
ax = sns.distplot(tips["total_bill"]) # 밀도함수 + 히스토그램 (kde = False : 밀도함수를 제외하고 출력, hist = False : 히스토그램 제외하고 출력 )
ax.set_title("Total Bill Histogram with Density plot")
plt.show()

ax = plt.subplot()
ax = sns.countplot("day", data = tips)
ax.set_title("Count of days")
ax.set_xlabel("Day of the Week")
ax.set_ylabel("Frequency")
plt.show()

ax = plt.subplot()
ax = sns.regplot(x = "total_bill", y = "tip", data = tips) # 추세선 포함 (geom_smooth function in R), fit_reg = False : 추세선 제거
ax.set_title("Scatterplot of Total Bill and Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")
plt.show()

joint = sns.jointplot(x = "total_bill", y = "tip", data = tips) # 산점도와 히스토그램을 같이 출력해줌
joint.set_axis_labels(xlabel = "Total Bill", ylabel = "Tip")
joint.fig.suptitle("Joint Plot of Total Bill and Tip", fontsize = 10, y = 1.03)
plt.show()

hexbin = sns.jointplot(x = "total_bill", y = "tip", data = tips , kind = "hex") # kind = "hex" : 핵사곤 형태의 히트멥으로 표현
hexbin.set_axis_labels(xlabel = "Total Bill", ylabel = "Tip")
hexbin.fig.suptitle("Hexbin Joint Plot of Total Bill and Tip", fontsize = 10, y = 1.03)
plt.show()

ax = plt.subplot()
ax = sns.kdeplot(data = tips["total_bill"], # 밀도추정 함수로 출력
                 data2 = tips["tip"],
                 shade = True)
ax.set_title("Kernel Density Plot of Total Bill and Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")
plt.show()

ax = plt.subplot()
ax = sns.barplot(x = "time", y = "total_bill", data = tips)
ax.set_title("Bar plot of average total bill for time of day")
ax.set_xlabel("Time of day")
ax.set_ylabel("Average total Bill")
plt.show()

ax = plt.subplot()
ax = sns.boxplot(x = "time", y = "total_bill", data = tips)
ax.set_title("BOxplot of total bill by time of day")
ax.set_xlabel("Time of day")
ax.set_ylabel("Total Bill")
plt.show()

ax = plt.subplot()
ax = sns.violinplot(x = "time", y = "total_bill", data = tips)
ax.set_title("Violin plot of total bill by time of day")
ax.set_xlabel("Time of day")
ax.set_ylabel("Total Bill")
plt.show()

fig = sns.pairplot(tips)
plt.show()

# pair_grid = sns.PairGrid(tips)
# pair_grid = pair_grid.map_upper(sns.regplot)
# pair_grid = pair_grid.map_lower(sns.kdeplot)
# pair_grid = pair_grid.map_diag(sns.distplot, rug=True)
# plt.show()

ax = plt.subplot()
ax = sns.violinplot(x = "time", y = "total_bill", data = tips,
                    hue = "sex",
                    split = True) # hue = col function in R
plt.show()

scatter = sns.lmplot(x = "total_bill", y= "tip", data = tips,
                     hue = "sex",
                     fit_reg = False)
plt.show()

fig = sns.pairplot(tips, hue = "sex")
plt.show()

scatter = sns.lmplot(x = "total_bill", y = "tip", data = tips,
                     fit_reg = False,
                     hue = "sex",
                     scatter_kws = {"s" : tips["size"] * 10}) # scatter_kws = size function in R
plt.show()

sctter = sns.lmplot(x = "total_bill", y = "tip",  data = tips,
                    fit_reg = False,
                    hue = "sex",
                    markers = ["o", "x"],
                    scatter_kws = {"s" : tips["size"] * 10})

anscombe_plot = sns.lmplot(x = "x", y = "y", data = anscombe,
                           fit_reg = False,
                           col = "dataset",
                           col_wrap = 2)
plt.show() # col_wrap = facet_wrap function in R

facet = sns.FacetGrid(tips, col = "time")
facet.map(sns.distplot, "total_bill", rug = True)
plt.show()

facet = sns.FacetGrid(tips, col='day', hue='sex')
facet = facet.map(plt.scatter, 'total_bill', 'tip')
facet = facet.add_legend()
plt.show()

facet = sns.FacetGrid(tips, col = "time", row = "smoker", hue = "sex")
facet.map(plt.scatter, "total_bill", "tip")
plt.show()

# + [ 4.4 ] ===================
ax = plt.subplot()
ax = tips["total_bill"].plot.hist()
plt.show()

fig, ax = plt.subplots()
ax = tips[["total_bill", "tip"]].plot.hist(alpha = 0.5, bins = 20, ax = ax)
plt.show()

ax = plt.subplots()
ax = tips["tip"].plot.kde()
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.scatter(x = "total_bill", y = "tip", ax = ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.hexbin(x = "total_bill", y = "tip", ax = ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.hexbin(x = "total_bill", y = "tip", gridsize = 10, ax = ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.box(ax = ax)
plt.show()

# + [ 4.5 ] ===================
sns.set_style("whitegrid")
fig, ax = plt.subplots()
ax = sns.violinplot(x = "time", y = "total_bill", hue = "sex", data = tips, split = True)
plt.show()

fig = plt.figure()
seaborn_styles = ["darkgrid", "whitegrid", "dark", "white", "ticks"]

for idx, style in enumerate(seaborn_styles) :
    plot_position = idx + 1
    with sns.axes_style(style) :
        ax = fig.add_subplot(2, 3, plot_position)
        violin = sns.violinplot(x = "time", y = "total_bill", data = tips, ax = ax)
        violin.set_title(style)

fig.tight_layout()
plt.show()