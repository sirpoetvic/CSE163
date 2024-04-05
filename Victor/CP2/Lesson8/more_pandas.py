"""more_pandas"""

# https://cse163.github.io/book/module-3-pandas/lesson-8-more-pandas/practice-more-pandas/PandasPractice.html

import pandas as pd

df = pd.read_csv("Victor\\CP2\\ufos.csv")

# Problem 0
ans0 = df.groupby("shape")["duration (seconds)"].mean()

# Problem 1
ans1 = (
    df[(df["latitude"] > 0) | (df["longitude"] > 0)]
    .groupby("city")["duration (seconds)"]
    .max()
)

# Problem 2
ans2 = df.groupby("city")["duration (seconds)"].sum().idxmax()


# Problem 3
ans3 = df["comments"].apply(lambda x: len(x.split(" ")))
