"""
Your name
class
file description
"""

import os
import tempfile
from matplotlib import legend
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()


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
    plot_hispanic_min_degree(data)
    # Call your functions here


def compare_bachelors_1980(data):
    """
    Computes the percentages of men and women who achieved a minimum of a Bachelor's
    degree in 1980.

    Args:
        data (DataFrame): DataFrame of csv
    """
    # Mask considers only bachelor degrees, 1980 as year, and M/F.
    mask = (
        (data["Min degree"] == "bachelor's")
        & (data["Year"] == 1980)
        & ((data["Sex"] == "M") | (data["Sex"] == "F"))
    )
    # Apply mask on data
    masked_data = data[mask]
    # Using the new dataset, take only sex and total columns
    # Note: This was my best attempt to print the DataFrame without the indexes
    # This function prints, rather than returning the df.
    # It also prints it as strings
    df = masked_data.loc[:, ["Sex", "Total"]].to_string(index=False)
    print(df)


def top_2_2000s(data, sex="A"):
    """
    Computes the two most commonly earned degrees for a given sex
    between the years 2000 and 2010 (inclusive).

    Args:
        data (DataFrame): DataFrame of csv
        sex (str, optional): Sex to sort data by. Defaults to "A".

    Returns:
        Series: _description_
    """
    # Mask considers data whose year is between 2000 and 2010 inclusive,
    # and sex as given sex
    mask = (data["Year"] >= 2000) & (data["Year"] <= 2010) & (data["Sex"] == sex)
    # Applying mask
    masked_data = data[mask]
    # Grouping by the min degree, using the mean of percentage over all of
    # the years, take the 2 largest min degrees
    return masked_data.groupby("Min degree")["Total"].mean().nlargest(2)


def line_plot_bachelors(data):
    mask = (data["Sex"] == "A") & (data["Min degree"] == "bachelor's")
    sns.set()
    sort_data = data[mask].loc[:, ["Year", "Min degree", "Total"]].dropna()
    sns.relplot(data=sort_data, x="Year", y="Total", kind="line")
    plt.title("Percentage Earning Bachelor's over Time")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.savefig("Victor\\HW3\\line_plot_bachelors.png", bbox_inches="tight")


def bar_chart_high_school(data):
    year = data["Year"] == 2009
    min_degree = data["Min degree"] == "high school"
    mask = data[year & min_degree]
    sns.catplot(data=mask, kind="bar", x="Sex", y="Total", hue="Sex")
    plt.title("Percentage Completed High School by Sex")
    plt.xlabel("Sex")
    plt.ylabel("Percentage")
    plt.savefig("Victor\\HW3\\bar_chart_high_school.png", bbox_inches="tight")


def plot_hispanic_min_degree(data):
    year = (data["Year"] >= 1990) & (data["Year"] <= 2010)
    hs = data["Min degree"] == "high school"
    b = data["Min degree"] == "bachelor's"
    hs_mask = data[year & hs]
    b_mask = data[year & b]

    first = sns.regplot(data=hs_mask, x="Year", y="Hispanic", label="High School")
    second = sns.regplot(data=b_mask, x="Year", y="Hispanic", label="Bachelor's")
    plt.title("Percentage of ")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.xticks([1990, 1995, 2000, 2005, 2010])
    plt.title(
        "Percentages of Hispanic degrees from 1990-2010 (High School & Bachelor's)"
    )
    plt.legend()
    plt.savefig("Victor\\HW3\\plot_hispanic_min_degree.png", bbox_inches="tight")


def fit_and_predict_degrees(data):
    pre_filter = ["Year", "Min degree", "Sex", "Total"]
    data = data.loc[:, pre_filter].dropna()
    features = pd.get_dummies(data)


if __name__ == "__main__":
    main()
