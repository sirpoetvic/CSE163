from pyexpat import features
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def problem_0():
    data = pd.read_csv("Victor\\CP3\\mushrooms.csv")
    return data


def problem_1(data):
    # Select all non-blank rows, with given columns
    features_col = ["cap-shape", "cap-surface", "cap-color", "class"]
    data = data.loc[:, features_col].dropna()
    features = pd.get_dummies(data.loc[:, data.columns != "class"])
    labels = data["class"]

    # 70% Training, 30% Testing
    features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.3
    )
    return (features_train, features_test, labels_train, labels_test)


def problem_2(features_train, labels_train):
    model = DecisionTreeClassifier()

    # Train it on training data
    model.fit(features_train, labels_train)

    train_predictions = model.predict(features_train)

    train_acc = accuracy_score(labels_train, train_predictions)

    return (model, train_acc)


def problem_3(model, features_test, labels_test):
    train_predictions = model.predict(features_test)
    train_acc = accuracy_score(labels_test, train_predictions)

    return train_acc


def main():
    df = problem_0()
    features_train, features_test, labels_train, labels_test = problem_1(df)
    test_acc, train_acc = problem_2(features_train, labels_train)
    print(len(features_train), len(features_test))
    print(len(labels_train), len(labels_test))
    print(features_train.columns)

    model, train_accuracy = problem_2(features_train, labels_train)
    print("Train accuracy:", train_accuracy)

    test_accuracy = problem_3(model, features_test, labels_test)
    print("Test Accuracy:", test_accuracy)


main()
