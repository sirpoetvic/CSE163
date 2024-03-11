# Import pandas
import pandas as pd

# Import the model
from sklearn.tree import DecisionTreeClassifier

# Import the function to compute accuracy
from sklearn.metrics import accuracy_score

# Read in data
data = pd.read_csv("Victor\\CP3\\homes.csv")

# Separate data into features and labels
features = data.loc[:, data.columns != "city"]
labels = data["city"]

# Create an untrained model
model = DecisionTreeClassifier()
# Train it on our training data
model.fit(features, labels)

# Make predictions on the data
predictions = model.predict(features)
# Assess the accuracy of the model
accuracy_score(labels, predictions)
