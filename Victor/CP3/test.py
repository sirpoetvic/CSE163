import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Victor\\CP3\\fmri.csv")

sns.relplot(x="petal_width", y="petal_length", title="Petal Width vs Length")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Petal Length (cm)")

plt.show()
