import pandas as pd

df = pd.read_csv('William\\CP2\\tas.csv')
ans1 = df["Salary"].max() - df["Salary"].min()

df2 = pd.read_csv('William\\CP2\\emissions.csv')
df2["per_capita"] = df2["emissions"] / df2["population"]
ans2 = df2["per_capita"].max()

high_pop = df2['population'] > 50
is_france = df2['country'] == 'France'
ans3 = df2[high_pop & is_france]
