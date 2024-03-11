import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()  # Don't forget this!
data = pd.read_csv("Victor\\CP3\\iris.csv")
sns.relplot(data=data, x="petal_width", y="petal_length", hue="species")
plt.title("Petal Width vs Length")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
