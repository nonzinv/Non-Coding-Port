"""
Non Pronanun
CSE 163 AD

Thi file contains methods that calculates certain points of analysis and graphs
according to the directions in A4. The methods include: compare_bachelors_1980,
plot_hispanic_min_degree, bar_chart_high_school, line_plot_bachelors,
top_2_2000s, and fit_and_predict_degrees.
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# Your imports here
sns.set()


# Define your functions here
def compare_bachelors_1980(df: pd.DataFrame) -> pd.DataFrame:
    """
    This method takes in a dataframe and returns another dataframe.
    The function of it is to compare the number of people with atleast
    a bachelor's degree in 1980, separated by gender.
    """
    year = df['Year'] == 1980
    bachelor = df['Min degree'] == 'bachelor\'s'
    sex = (df['Sex'] == 'M') | (df['Sex'] == 'F')
    result = df[year & bachelor & sex][['Sex', 'Total']]
    return result


def top_2_2000s(df: pd.DataFrame, sex: str = 'A') -> pd.Series:
    """
    This method takes in a dataframe and optionally a string, it returns
    a series. The function of it is to find what is the  two most common level
    of education in the 2000s, by sex (the string that is passed in). If no
    string is passed in, it defaults to all genders.
    """
    year = (df['Year'] >= 2000) & (df['Year'] <= 2010)
    sex = df['Sex'] == sex
    filtered = df[year & sex]
    result = filtered.groupby('Min degree')['Total'].mean()
    return result.nlargest(2)


def line_plot_bachelors(df: pd.DataFrame) -> None:
    """
    This method takes in a dataframe, and returns None. The function
    of it is to create a lineplot showing the trend of people with
    atleast a bachelor's degree over the years.
    """
    df = df[(df['Sex'] == 'A') & (df['Min degree'] == 'bachelor\'s')]
    sns.relplot(data=df, x='Year', y='Total', kind='line')
    plt.title('Percentage Earning Bachelor\'s over Time')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(df: pd.DataFrame) -> None:
    """
    This program takes in a dataframe, and returns None. The function of
    it is to create a bar chart showing the number of people with atleast
    a high school diploma in 2009 separated by sex.
    """
    df = df[(df['Year'] == 2009) & (df['Min degree'] == 'high school')]
    sns.catplot(data=df, x='Sex', y='Total', kind='bar')
    plt.title('Percentage Completed High School by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(df: pd.DataFrame) -> None:
    """
    This method takes in a dataframe, and returns None. The function
    of it is to create a lineplot showing the trend of Hispanics who
    are receiving high school or bachelor's education in the years between
    1990 and 2010
    """
    df = df[((df['Year'] >= 1990) & (df['Year'] <= 2010) &
            ((df['Min degree'] == 'high school') |
            (df['Min degree'] == 'bachelor\'s')))]
    sns.relplot(data=df, x='Year', y='Hispanic', kind='line', hue='Min degree',
                errorbar=None)
    plt.title('Hispanics with atleast High School education by year')
    plt.ylabel('Percentage')
    plt.xlabel('Year')
    years = [1990, 1995, 2000, 2005, 2010]
    plt.xticks(years)
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(df: pd.DataFrame) -> float:
    """
    This program takes a dataframe and returns a float. It creates
    an algorithm that predicts the percentage of people receiving each
    degree with a given characteristic (Sex, Year). It returns the
    percent error of this model to test the accuracy.
    """
    df = df[['Year', 'Min degree', 'Sex', 'Total']]
    df = df.dropna()
    df_dummies = df.loc[:, df.columns != 'Total']
    features = pd.get_dummies(df_dummies)
    labels = df['Total']
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    predictions = model.predict(features_test)
    return mean_squared_error(labels_test, predictions)


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    # Call your functions here
    compare_bachelors_1980(data)
    top_2_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()