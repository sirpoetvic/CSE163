import pandas as pd


def problem_0(df):

    ans0 = df.groupby('shape')['duration (seconds)'].mean()
    return ans0


def problem_1(df):

    pos_value = (df['latitude'] > 0) | (df['longitude'] > 0)
    ans1 = df[pos_value].groupby('city')['duration (seconds)'].max()
    return ans1


def problem_2(df):

    largest_duration = df.groupby('city')['duration (seconds)'].sum()
    ans2 = largest_duration.idxmax()
    return ans2


def problem_3(df):

    ans3 = df['comments'].str.split().str.len()
    return ans3


def main():

    df = pd.read_csv('William\\CP2\\ufos.csv')
    df = df.head()
    print(problem_0(df), "\n")
    print(problem_1(df), "\n")
    print(problem_2(df), "\n")
    print(problem_3(df))


if __name__ == '__main__':
    main()
