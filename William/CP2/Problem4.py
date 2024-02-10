import pandas as pd
import matplotlib.pyplot as plt


def problem_0():
    # your code here
    goog = pd.read_csv('William\\CP2\\google.csv',
                       index_col='Date', parse_dates=True)
    goog = goog.sort_index()
    return goog


def problem_1(df):

    # your code here
    df['Adj Close'].plot()
    # keep this as the last line of this method
    plt.savefig('William\\CP2\\prob1.png')


def problem_2(df):

    # your code here
    ans2 = df.loc['2019-10':'2020-04']
    # keep this as the last line of this method
    ans2['Adj Close'].plot()
    plt.savefig('William\\CP2\\prob2.png')


def problem_3(df):

    # your code here
    ans3 = df.resample('M').mean()
    # keep this as the last line of this method
    ans3['Adj Close'].plot()
    plt.savefig('William\\CP2\\prob3.png')


def problem_4(df):
    # your code here
    ans4 = df.rolling(window=14).mean()
    # keep this as the last line of this method
    ans4['Adj Close'].plot()
    plt.savefig('William\\CP2\\prob4.png')


def main():
    '''
    DO NOT CHANGE: Must be this way to pass the tests.

    We load the DataFrame in problem 0 then draw all the plots.
    We use plt.clf() to clear the current figure--to start fresh.
    Without plot.clf() we would continually overlay the plot onto the old plot.
    '''
    df = problem_0()
    plt.clf()
    problem_1(df)
    plt.clf()
    problem_2(df)
    plt.clf()
    problem_3(df)
    plt.clf()
    problem_4(df)


if __name__ == '__main__':
    main()
