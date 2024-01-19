# earthquakes

# https://cse163.github.io/book/module-3-pandas/lesson-7-introduction-to-pandas/practice-earthquakes/Earthquakes.html

import pandas as pd

df = pd.read_csv("C:\\Users\\victo\\OneDrive\\Desktop\\CSE163\\Victor\\CP2\\tas.csv")
ans1 = df["Salary"].max() - df["Salary"].min()
                