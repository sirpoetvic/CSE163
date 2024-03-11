import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def problem_0():
    data = pd.read_csv("Victor\\CP3\\mushrooms.csv")
    return data


def problem_1(data):
    # Select all non-blank rows, with given columns
    features = data.loc[:, ["cap-shape", "cap-surface", "cap-color"]].dropna()

    # Make sure that you select only from the features rows
    labels = data.loc[features.index, "class"]

    # 70% Training, 30% Testing
    features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.3
    )
    return features_train, features_test, labels_train, labels_test


def problem_2(features_train, features_test, labels_train, labels_test):
    model = DecisionTreeRegressor()

    # Train it on training data
    model.fit(features_train, labels_train)

    train_predictions = model.predict(features_train)
    test_predictions = model.predict(features_test)

    test_acc = accuracy_score(labels_test, test_predictions)
    train_acc = accuracy_score(labels_train, train_predictions)

    return test_acc, train_acc


def main():
    df = problem_0()
    features_train, features_test, labels_train, labels_test = problem_1(df)
    test_acc, train_acc = problem_2(
        features_train, features_test, labels_train, labels_test
    )
    print(test_acc)
    print(train_acc)


main()
