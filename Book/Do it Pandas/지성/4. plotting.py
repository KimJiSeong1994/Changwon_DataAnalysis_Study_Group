# ============================================== [ setting ] ====================================================
import seaborn as sns
import matplotlib.pyplot as plt

ancombe = sns.load_dataset("anscombe")

# ============================================== [ plotting ] ====================================================
# + [ 4.1 ] ===================
# dataset_1 = ancombe[ancombe["dataset"] == "I"]
# plt.plot(dataset_1["x"], dataset_1["y"])
# plt.show()
# plt.plot(dataset_1["x"], dataset_1["y"], "o") # `o` : scatter plot
# plt.show()

dataset_1 = ancombe[ancombe["dataset"] == "I"]
dataset_2 = ancombe[ancombe["dataset"] == "II"]
dataset_3 = ancombe[ancombe["dataset"] == "III"]
dataset_4 = ancombe[ancombe["dataset"] == "IV"]

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