"""pandas_tutorial"""

# https://cse163.github.io/book/module-3-pandas/lesson-7-introduction-to-pandas/practicereading-pandas-tutorial/PandasTutorial.html

import pandas as pd

df = pd.read_csv("Victor\\CP2\\Lesson7\\tas.csv")
df2 = pd.read_csv("Victor\\CP2\\Lesson7\\emissions.csv")


# Problem 0: access the Salary column of tas.csv
ans0 = df["Salary"]


# Problem 1: compute range of TA salaries
ans1 = df["Salary"].max() - df["Salary"].min()


# Problem 2: compute max emissions per capita
df2["per_capita"] = df2["emissions"] / df2["population"]
ans2 = df2["per_capita"].max()

# Problem 3: select all rows in France and population > 50
ans3 = (df2["country"] == "France") & (df2["population"] > 50)
