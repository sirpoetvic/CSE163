"""coding_machine_learning_2"""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def problem_0() -> pd.DataFrame:
    """Load in the dataset into a DataFrame named data. Don't preprocess the
    data in any way for this problem.

    Returns:
        DataFrame: read CSV "mushrooms.csv"
    """
    data = pd.read_csv("Victor\\CP3\\Lesson12\\mushrooms.csv")
    return data


def problem_1(data: pd.DataFrame) -> tuple:
    """
    Drop all columns that are not relevant to the analysis.
    Remove all rows that have missing values for the columns
    of interest. There is no need to throw out rows that have
    missing values outside of these 4 columns (since those missing
    values will not be included in the model).
    Separate the data into usable features and labels.
    Split the dataset into 70% training data and 30% test data.

    Args:
        data (DataFrame): _description_

    Returns:
        tuple: contains training/testing features & labels
    """
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
    """
    Write code to create a decision tree model and train it.
    Make sure you save it in a variable called model.

    Args:
        features_train (_type_): _description_
        labels_train (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = DecisionTreeClassifier()

    # Train it on training data
    model.fit(features_train, labels_train)

    train_predictions = model.predict(features_train)

    train_acc = accuracy_score(labels_train, train_predictions)

    return (model, train_acc)


def problem_3(model, features_test, labels_test):
    """
    Write code to compute the training and test accuracy of the model in the
    cell below. Save the train accuracy in varaible called train_acc and the
    test accuracy in a variable called test_acc.

    For reference, each of your train and test accuracies should be around 70%.

    Args:
        model (DataFrame)
        features_test ()
        labels_test (_type_): _description_

    Returns:
        _type_: _description_
    """
    train_predictions = model.predict(features_test)
    train_acc = accuracy_score(labels_test, train_predictions)

    return train_acc


"""

"""


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
