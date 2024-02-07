import pandas as pd

df = pd.read_csv('William\\CP2\\earthquakes.csv')

ans0 = df['magnitude'].mean()
print(ans0)

ans1 = df['magnitude'] > ans0
print(len(df[ans1]))

combined_rows = df[
    (df['name'] == 'Tonga') | (df['name'] == 'Papua New Guinea')]
ans2 = combined_rows[combined_rows['day'] == 8]
print(ans2)

max_index = df['magnitude'].idxmax()
ans3 = df.loc[max_index, :]
print(ans3)
