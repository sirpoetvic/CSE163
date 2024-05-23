"""earthquakes"""

# https://cse163.github.io/book/module-3-pandas/lesson-7-introduction-to-pandas/practice-earthquakes/Earthquakes.html

import pandas as pd

df = pd.read_csv("Victor\\CP2\\Lesson7\\earthquakes.csv")

# Problem 0: Compute average magnitude of all earthquakes in dataset
ans0 = df["magnitude"].mean()

# Problem 1: Compute num of earthquakes with mag greater/equal to avg magnitude
greater_than_avg = df["magnitude"] > df["magnitude"].mean()
ans1 = len(df[greater_than_avg])

# Problem 2: Find subset of earthquakes that happened on the 8th day of
# the month in Tonga or Papua New Guinea
tonga_or_png = (df["name"] == "Tonga") | (df["name"] == "Papua New Guinea")
day_8 = df["day"] == 8
ans2 = df[tonga_or_png & day_8]

# Problem 3: Find the row that corresponds to the location that has the largest
# earthquake on record
largest_earthquake = df["magnitude"].idxmax()
ans3 = df.loc[largest_earthquake]
