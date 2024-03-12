'''
Your name
class
file description
'''

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
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    sns.set_theme()
    # Call your functions here


if __name__ == '__main__':
    main()