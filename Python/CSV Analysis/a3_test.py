"""
Non Pronanun
CSE 163 AD

This file runs the tests for the different methods in a3_manual and
a3_pandas, it tests whether or not the methods written in each file is
working correctly according to the spec.
"""


import pandas as pd

from cse163_utils import assert_equals, parse, Pokemon

import a3_manual
import a3_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"
MORE_TEST = "/home/extra_test.csv"


# Your tests here!
def test_species_count(data_manual: list[Pokemon],
                       data_pandas: pd.DataFrame,
                       new_data_manual: list[Pokemon],
                       new_data_pandas: pd.DataFrame) -> None:
    """
    This method tests the correctness of the species_count method
    in both of the implementations.
    """
    # Feel free to edit this function and its parameters
    # to test your own datasets too
    assert_equals(3, a3_manual.species_count(data_manual))
    assert_equals(3, a3_pandas.species_count(data_pandas))
    assert_equals(3, a3_manual.species_count(new_data_manual))
    assert_equals(3, a3_pandas.species_count(new_data_pandas))
    pass


def test_max_level(data_manual: list[Pokemon],
                   data_pandas: pd.DataFrame,
                   new_data_manual: list[Pokemon],
                   new_data_pandas: pd.DataFrame) -> None:
    """
    This method tests the correctness of the max_level method
    in both of the implementations.
    """
    # Feel free to edit this function and its parameters
    # to test your own datasets too
    assert_equals(('Lapras', 72), a3_manual.max_level(data_manual))
    assert_equals(('Lapras', 72), a3_pandas.max_level(data_pandas))
    assert_equals(('Marowak', 40), a3_manual.max_level(new_data_manual))
    assert_equals(('Marowak', 40), a3_pandas.max_level(new_data_pandas))
    pass


def test_filter_range(data_manual: list[Pokemon],
                      data_pandas: pd.DataFrame,
                      new_data_manual: list[Pokemon],
                      new_data_pandas: pd.DataFrame) -> None:
    """
    This method tests the correctness of the filter_range method
    in both of the implementations.
    """
    # Feel free to edit this function and its parameters
    # to test your own datasets too
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  a3_manual.filter_range(data_manual, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  a3_pandas.filter_range(data_pandas, 35, 72))
    assert_equals(['Cubone', 'Cubone'],
                  a3_manual.filter_range(new_data_manual, 15, 31))
    assert_equals(['Cubone', 'Cubone'],
                  a3_pandas.filter_range(new_data_pandas, 15, 31))
    pass


def test_mean_attack_for_type(data_manual: list[Pokemon],
                              data_pandas: pd.DataFrame,
                              new_data_manual: list[Pokemon],
                              new_data_pandas: pd.DataFrame) -> None:
    """
    This method tests the correctness of the mean_attack_for_type method
    in both of the implementations.
    """
    # Feel free to edit this function and its parameters
    # to test your own datasets too
    assert_equals(47.5, a3_manual.mean_attack_for_type(data_manual, 'fire'))
    assert_equals(47.5, a3_pandas.mean_attack_for_type(data_pandas, 'fire'))
    assert_equals(105.0, a3_manual.mean_attack_for_type(new_data_manual,
                                                        'ground'))
    assert_equals(105.0, a3_pandas.mean_attack_for_type(new_data_pandas,
                                                        'ground'))
    pass


def test_count_types(data_manual: list[Pokemon],
                     data_pandas: pd.DataFrame,
                     new_data_manual: list[Pokemon],
                     new_data_pandas: pd.DataFrame) -> None:
    """
    This method tests the correctness of the count_types method
    in both of the implementations.
    """
    # Feel free to edit this function and its parameters
    # to test your own datasets too
    assert_equals({'fire': 2, 'water': 2}, a3_manual.count_types(data_manual))
    assert_equals({'fire': 2, 'water': 2}, a3_pandas.count_types(data_pandas))
    assert_equals({'ground': 3, 'normal': 1},
                  a3_manual.count_types(new_data_manual))
    assert_equals({'ground': 3, 'normal': 1},
                  a3_pandas.count_types(new_data_pandas))
    pass


def test_mean_attack_per_type(data_manual: list[Pokemon],
                              data_pandas: pd.DataFrame,
                              new_data_manual: list[Pokemon],
                              new_data_pandas: pd.DataFrame) -> None:
    """
    This method tests the correctness of the mean_attack_per_type method
    in both of the implementations.
    """
    # Feel free to edit this function and its parameters
    # to test your own datasets too
    assert_equals({'fire': 47.5, 'water': 140.5},
                  a3_manual.mean_attack_per_type(data_manual))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  a3_pandas.mean_attack_per_type(data_pandas))
    assert_equals({'ground': 105.0, 'normal': 20.0},
                  a3_manual.mean_attack_per_type(new_data_manual))
    assert_equals({'ground': 105.0, 'normal': 20.0},
                  a3_pandas.mean_attack_per_type(new_data_pandas))
    pass


def main():
    """
    This is the main method that runs all of the tests above.
    """
    data_manual: list[Pokemon] = parse(SPEC_TEST_FILE)
    data_pandas: pd.DataFrame = pd.read_csv(SPEC_TEST_FILE)
    new_data_manual: list[Pokemon] = parse(MORE_TEST)
    new_data_pandas: pd.DataFrame = pd.read_csv(MORE_TEST)
    print(data_manual)
    test_species_count(data_manual, data_pandas, new_data_manual,
                       new_data_pandas)
    test_max_level(data_manual, data_pandas, new_data_manual,
                   new_data_pandas)
    test_filter_range(data_manual, data_pandas, new_data_manual,
                      new_data_pandas)
    test_mean_attack_for_type(data_manual, data_pandas, new_data_manual,
                              new_data_pandas)
    test_count_types(data_manual, data_pandas, new_data_manual,
                     new_data_pandas)
    test_mean_attack_per_type(data_manual, data_pandas, new_data_manual,
                              new_data_pandas)


if __name__ == "__main__":
    main()