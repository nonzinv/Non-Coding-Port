"""
Non Pronanun
CSE 163 AD

This is a file that runs the programs according to the spec in Pokemon, this
file runs all the programs using pandas and data frames. The input here is
predominantly pd.DataFrame
"""


import pandas as pd


# Your code here!
def species_count(df: pd.DataFrame) -> int:
    """
    This method takes in a DataFrame of Pokemons. It counts the number of
    different species of Pokemon is in the file.
    """
    unique = df['name'].unique()
    return len(unique)


def max_level(df: pd.DataFrame) -> tuple[str, int]:
    """
    This method takes in a DataFrame. It finds the Pokemon with
    the highest level and returns the name of the Pokemon, as well as
    the level.
    """
    index = df['level'].idxmax()
    pokemon = df.loc[index, 'name']
    level = df.loc[index, 'level']
    return (pokemon, level)


def filter_range(df: pd.DataFrame, range_min: int,
                 range_max: int) -> list[str]:
    """
    This method takes in a DataFrame and range. It finds the Pokemons
    in the dataframe that is in between the range that is given. The result
    is a list of names of the Pokemons that fit that range.
    """
    lower_bound = df['level'] >= range_min
    upper_bound = df['level'] < range_max
    filtered = df[lower_bound & upper_bound]
    result = list(filtered.loc[:, 'name'])
    return result


def mean_attack_for_type(df: pd.DataFrame, s: str) -> float | None:
    """
    This method takes in a DataFrame of Pokemons and a string. It returns
    the average attack of Pokemons with the type that is inputted by the
    string. In the case that there are no Pokemons of that type in the
    dataframe, it returns None.
    """
    is_type = df[(df['type'] == s)]
    if is_type.empty:
        return None
    return is_type['atk'].mean()


def count_types(df: pd.DataFrame) -> dict[str, int]:
    """
    This method takes in a DataFrame of Pokemons. This programs
    counts the number of Pokemons in each type given in the DataFrame.
    The result is returned as a dictionary of the Type and the number of
    Pokemons with that type.
    """
    return dict(df.groupby('type')['type'].count())


def mean_attack_per_type(df: pd.DataFrame) -> dict[str, float]:
    """
    This method takes in a DataFrame of Pokemons. This program lists
    the different types of Pokemon in the DataFrame as well as the
    average attack of each of the types. It returns a dictionary of
    the type and the float for each type's average attack.
    """
    return dict(df.groupby('type')['atk'].mean())