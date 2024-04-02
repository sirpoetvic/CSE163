'''
This is the code found in Lesson 12:
  Practice: Coding Machine Learning

We will be using mushrooms.csv data.
'''

# import libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def load_data(file_name):
    '''
    problem 0: Load the Data

    Load in the dataset into a DataFrame and return it.
    Don't preprocess the data in any way here.
    '''
    df = pd.read_csv(file_name)
    return df


def process_data(df):
    '''
    Problem 1: Process the Data

    Do the data processing parts of the ML pipeline. Namely, do the following:

    * Drop all columns that are not relevant to the analysis.
    * Remove all rows that have missing values for the columns of interest.
    no need to throw out rows that have missing values outside of the 4 columns
    (since those missing values will not be included in the model).
    * Separate the data into usable features and labels.
    * Split the dataset into 70% training data and 30% test data.

    Return the features and labels as a tuple:
        (features_train, features_test, labels_train, labels_test)
    features: 'cap-shape', 'cap-surface', 'cap-color'
    lables: 'class'
    '''
    feature_col = ['cap-shape', 'cap-surface', 'cap-color', 'class']
    df = df.loc[:, feature_col].dropna()
    features = df.loc[:, df.columns != 'class']
    features = pd.get_dummies(features)
    labels = df['class']

    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.3)

    return (features_train, features_test, labels_train, labels_test)


def train_the_model(features_train, labels_train):
    '''
    Problem 2: Train the Model

    Write code to create a decision tree model and train it.
    You will also assess the training accuracy of the model here.
    For reference, your train accuracy should be around 70%.

    Return a tuple:
        (model, train_accuracy)
    '''
    features_train = pd.get_dummies(features_train)

    model = DecisionTreeClassifier()
    model.fit(features_train, labels_train)

    train_prediction = model.predict(features_train)
    train_accuracy = accuracy_score(labels_train, train_prediction)

    return (model, train_accuracy)


def assess_the_model(model, features_test, labels_test):
    '''
    Problem 3: Assess the model

    Write code to compute the test accuracy of the model.
    Return the train accuracy.

    For reference, your test accuracy should be around 70%.
    '''
    train_prediction = model.predict(features_test)
    train_accuracy = accuracy_score(labels_test, train_prediction)

    return train_accuracy


def main():
    df = load_data('William\\CP3\\mushrooms.csv')
    features_train, features_test, labels_train, labels_test = process_data(df)
    print(len(features_train), len(features_test))
    print(len(labels_train), len(labels_test))
    print(features_train.columns)

    model, train_accuracy = train_the_model(features_train, labels_train)
    print('Train accuracy:', train_accuracy)

    test_accuracy = assess_the_model(model, features_test, labels_test)
    print('Test Accuracy:', test_accuracy)


if __name__ == '__main__':
    main()
