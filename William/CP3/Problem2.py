import pandas as pd


def problem1(df):
    df = df.head()
    ans0 = df['magnitude'].mean()
    return ans0


def problem2(df):
    df = df.head()
    ans1 = df['magnitude'] > df['magnitude'].mean()
    return (len(df[ans1]))


def problem3(df):
    combined_rows = df[
        (df['name'] == 'Tonga') | (df['name'] == 'Papua New Guinea')]
    ans2 = combined_rows[combined_rows['day'] == 8]
    return (ans2)


def problem4(df):
    max_index = df['magnitude'].idxmax()
    ans3 = df.loc[max_index, :]
    return ans3


def main():
    df = pd.read_csv('William\\CP2\\earthquakes.csv')
    print(problem1(df))
    print(problem2(df))
    print(problem3(df))
    print(problem4(df))


if __name__ == '__main__':
    main()
