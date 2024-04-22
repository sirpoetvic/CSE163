"""
Your name
class
file description
"""

import os
import tempfile

os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()

import pandas as pd
import seaborn as sns

# Your imports here


# Define your functions here
# def compare_bachelors_1980
# def top_2_2000s
# def line_plot_bachelors
# def bar_chart_high_school
# def plot_hispanic_min_degree
# def fit_and_predict_degrees


def main():
    data = pd.read_csv("Victor\\HW3\\nces-ed-attainment.csv", na_values=["---"])
    sns.set()
    print(compare_bachelors_1980(data))
    # Call your functions here


def compare_bachelors_1980(data):
    mask = data[
        (data["Min degree"] == "bachelor's")
        & (data["Year"] == 1980)
        & ((data["Sex"] == "M") | (data["Sex"] == "F"))
    ]
    return mask.loc[:, ["Sex", "Total"]]


def top_2_2000s(data, sex="A"):
    mask = data.groupby("Min degree")["Sex"].mean()


if __name__ == "__main__":
    main()
