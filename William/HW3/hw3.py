'''
William Dinh
CSE 163
HW3 assignment
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Your imports here


# Define your functions here
def compare_bachelors_1980(data):
    """
    What were the percentages for women
    vs. men having earned a Bachelors Degree in 1980?
    Returns dataframe with % of men and women
    who attained a bachelor degree in 1980.
    Args:
        data (DataFrame) = to be modified and filtered
    """
    # Filter the data for Bachelor's degrees in or more 1980 for both sexes
    sort_grad = data[
        (data['Year'] == 1980) & (data['Min degree'] == "bachelor's")]
    # Sorts columns by sex and total
    sort_data = sort_grad.loc[:, ['Sex', 'Total']]
    # Takes columns previously, sorts by M and F, then sums the total
    # Which is the %. sort_gender is a series, split like this for flake8 sake
    sort_gender = sort_data[
        (sort_data['Sex'] == 'M') | (
            sort_data['Sex'] == 'F')].groupby('Sex')['Total'].sum()
    # convert sort_gender into a dataframe again
    df = pd.DataFrame(sort_gender, columns=['Total'])
    return df


def top_2_2000s(data, sex='A'):
    """
    Computes the two most commonly earned degrees for that given
    sex between the years 2000 and 2010 (inclusive)

    Compare educational attainment levels by using the mean
    Returns 2-element series with index on the left and value on the right
    Args:
        data (DataFrame) = to be modified and filtered
        sex (string) = Male (m), Female (f), or default Annonymous (a)
    """
    # sorts data for years between 2000 and 2010 (inclusive)
    filtered_data = data[(data['Year'] > 2000) & (data['Year'] <= 2010)]
    sort_data = filtered_data.loc[:, ['Min degree', 'Sex', 'Total']]
    # sorts data by sex
    by_sex = sort_data[sort_data['Sex'] == sex]
    # finds the two biggest means for attainment, based on degree
    most_common = by_sex.groupby(
        'Min degree')['Total'].mean().nlargest(2)
    return most_common


def line_plot_bachelors(data):
    """
    Takes in data, plots a line chart of the total percentages of all people
    Sex A with bachelor's Min degree over time.
    Label the x-axis Year, the y-axis Percentage,
    and title the plot Percentage Earning Bachelors over Time.
    """
    # filter data for Sex A, bachelor's
    filtered_data = data[
        (data['Min degree'] == "bachelor's") & (data['Sex'] == 'A')]
    # sort data with year, min degree, and total, with previous filters
    sort_data = filtered_data.loc[:, ['Year', 'Min degree', 'Total']].dropna()
    sns.relplot(data=sort_data, x='Year', y='Total', kind="line")
    # labeling axises
    plt.title("Percentage Earning Bachelor's over Time")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    # saving and displaying plot to plots folder in HW3
    plt.savefig('William\\HW3\\plots\\line_plot_bachelors.png',
                bbox_inches='tight')


def bar_chart_high_school(data):
    """
    Plots a bar chart comparing the total percentages of
    Sex F, M, and A with high school Min degree in the Year 2009
    """
    filtered_data = data[
        (data['Min degree'] == "high school") & (data['Year'] == 2000)]
    # box plot, with "sex" having different colors
    # assiging x with 'Sex' gives us all 3 (A, M, F)
    sns.catplot(data=filtered_data, kind="bar", x='Sex', y='Total')
    # label axises
    plt.title("Percentage Completed High School by Sex")
    plt.xlabel("Sex")
    plt.ylabel("Percentage")
    plt.savefig('William\\HW3\\plots\\bar_chart_high_school.png',
                bbox_inches='tight')


def plot_hispanic_min_degree(data):
    """
    Plots how the percentage of Hispanic people with degrees have changed
    between 1990-2010 (inclusive) for high school and bachelor's Min degree.
    Choose a plot type for this problem and prepare to explain your decision
    process in the writeup. Label the axes and title the plot appropriately.

    Graph chosen: linear regression plot, as we are comparing
    """

    # filter & sort data for 1990 to 2010 FOR ONLY bachelors
    filtered_data1 = data[
        ((data['Year'] >= 1990) & (data['Year'] <= 2010)) &
        ((data['Min degree'] == "bachelor's"))]
    sort_data1 = filtered_data1.loc[:,
                                    ["Year", "Min degree", "Hispanic"]]
    # filter  & sort data for 1990 to 2010 FOR ONLY high school
    filtered_data2 = data[
        ((data['Year'] >= 1990) & (data['Year'] <= 2010)) &
        ((data['Min degree'] == "high school"))]
    sort_data2 = filtered_data2.loc[:,
                                    ["Year", "Min degree", "Hispanic"]]

    # plot two regression plots, with each respective dataframe
    sns.regplot(data=sort_data1, x='Year', y='Hispanic', label="Bachelor's")
    sns.regplot(data=sort_data2, x='Year', y='Hispanic', label="High School")

    # label axises and legend
    plt.ylabel("Percentage")
    plt.xlabel("Year")
    plt.legend()
    # xticks custom x axis/years being double problem, also cleaner than before
    plt.xticks([1990, 1995, 2000, 2005, 2010])
    plt.title("%'s of Hispanic People with High School Or Bachelor's Degrees")
    plt.savefig('William\\HW3\\plots\\plot_hispanic_min_degree.png',
                bbox_inches='tight')


def fit_and_predict_degrees(data):
    pass


def main():
    data = pd.read_csv('William\\HW3\\nces-ed-attainment.csv',
                       na_values=['---'])
    sns.set_theme()
    # Call your functions here
    # print(compare_bachelors_1980(data))
    # print()
    # print(top_2_2000s(data, 'A'))
    # line_plot_bachelors(data)
    # bar_chart_high_school(data)
    plot_hispanic_min_degree(data)


if __name__ == '__main__':
    main()
