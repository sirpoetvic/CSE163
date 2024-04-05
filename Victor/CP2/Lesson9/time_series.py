"""time_series"""

# https://cse163.github.io/book/module-3-pandas/lesson-8-more-pandas/practice-more-pandas/PandasPractice.html

import pandas as pd
import matplotlib.pyplot as plt

# Problem 0
goog = pd.read_csv("Victor\\CP2\\google.csv", index_col="Date", parse_dates=True)

# Problem 1
goog["Adj Close"].plot()

# Problem 2:
ans2 = goog.loc["2019-10":"2020-04"]["Adj Close"]
ans2.plot()

# Problem 3``
ans3 = goog["Adj Close"].resample("ME").mean()
ans3.plot()

# Problem 4
ans4 = goog["Adj Close"].rolling(14).mean()
ans4.plot()

plt.show()
