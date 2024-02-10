import pandas as pd


def problem_1(df):
    ans1 = df["Salary"].max() - df["Salary"].min()
    return ans1


def problem_2(df2):
    df2["per_capita"] = df2["emissions"] / df2["population"]
    ans2 = df2["per_capita"].max()
    return ans2


def problem_3(df2):
    high_pop = df2['population'] > 50
    is_france = df2['country'] == 'France'
    ans3 = df2[high_pop & is_france]
    return ans3


def main():
    df = pd.read_csv('William\\CP2\\tas.csv')
    df2 = pd.read_csv('William\\CP2\\emissions.csv')
    print(problem_1(df))
    print(problem_2(df2))
    print(problem_3(df2))


if __name__ == '__main__':
    main()
