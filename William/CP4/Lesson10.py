import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme()


def part1():
    '''
    Instructions here:
    https://cse163.github.io/book/module-4-libraries-for-data-science/lesson-10-data-visualization/practice-plotting-1.html
    '''
    # TODO: Read data/iris.csv file using pandas library
    df = pd.read_csv('CP3\\iris.csv')

    # TODO: Plot petal_width vs petal_length using sns.replot and hue
    sns.relplot(x='petal_width',
                y='petal_length',
                hue='species',
                data=df)

    # TODO: Change the axis labels and title of the graph
    # x axis: "Petal Width (cm)"
    # y axis: "Petal Length (cm)"
    # Title: "Petal Width vs Length"
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.title('Petal Width vs Length')

    # Save the plot to a file
    # For this problem, we need an extra parameter for a better layout.
    plt.savefig('CP3\\lesson10_part1.png', bbox_inches='tight')


def part2():
    '''
    Instructions found here:
    https://cse163.github.io/book/module-4-libraries-for-data-science/lesson-10-data-visualization/practice-plotting-2.html
    '''
    plt.figure()  # using .figure(), we can run part1 and part2 simultaneously
    # TODO: Load data/iris_missing.csv
    df2 = pd.read_csv('CP3\\iris_missing.csv')
    # TODO: replace missing data with 0
    df2.fillna(0, inplace=True)
    # TODO: using regplot, Plot petal_length vs sepal_length
    sns.regplot(x='sepal_length',
                y='petal_length',
                color='g',
                data=df2)
    # TODO: set the axes labels and title
    plt.xlabel('Pedal Length (cm)')
    plt.ylabel('Sepal Length (cm)')
    plt.title('Pedal Length vs Sepal Length')
    # Save the figure to 'lesson10_part2.png'
    plt.savefig('CP3\\lesson10_part2.png', bbox_inches='tight')


def main():
    '''
    Runs part1 and part2 graphs
    '''
    part1()
    part2()


if __name__ == '__main__':
    main()
