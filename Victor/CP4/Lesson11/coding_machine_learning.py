# Import pandas
import pandas as pd

# Import the model
from sklearn.tree import DecisionTreeRegressor

# Import the function to compute accuracy
from sklearn.metrics import mean_squared_error

# Read in data
data = pd.read_csv("Victor\\CP3\\weather.csv")

# Separate data into features and labels
features = data.loc[:, data.columns != "MAX"]
labels = data["MAX"]

# Create an untrained model
model = DecisionTreeRegressor()
# Train it on our training data
model.fit(features, labels)

# Make predictions on the data
predictions = model.predict(features)
# Assess the accuracy of the model
error = mean_squared_error(labels, predictions)
print(error)
