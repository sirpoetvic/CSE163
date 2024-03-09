import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()  # Don't forget this!
data = pd.read_csv("Victor\\CP3\\iris_missing.csv")
data = data.fillna(0)
sns.regplot(data=data, x="petal_length", y="sepal_length", color="g")
plt.title("Petal Width vs Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sepal Length (cm)")
plt.show()
