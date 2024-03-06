import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


'''
** SEE INSTRUCTION DETAILS IN REPLIT INSTRUCTIONS **
** See full context at:
https://cse163.github.io/book/module-4-libraries-for-data-science/lesson-11-machine-learning/practice-coding-machine-learning/MLforWeather.html

This file is from Lesson 11:
  The last lesson: "Practice: Coding Machine Learning"


Create a Model to predict the maximum temperature of a day
given all the other information provided in the weather dataset.
Use DecisionTreeRegressor and mean_squared_error.
You should verify that the model has 0 error.
Return the model.
'''


def create_model():
    data = pd.read_csv('CP3\\weather.csv')
    features = data.loc[:, data.columns != 'MAX']
    labels = data['MAX']
    model = DecisionTreeRegressor()
    model.fit(features, labels)
    predictions = model.predict(features)
    error = mean_squared_error(labels, predictions)
    print('Model error:', error)
    return model


def main():
    create_model()


if __name__ == '__main__':
    main()
