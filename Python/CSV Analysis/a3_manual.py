"""
Non Pronanun
CSE 163 AD

This is a file that runs the programs according to the spec in Pokemon, this
file runs all the programs using dictionaries and standard python functions.
The input in this file is mainly dictionaries of Pokemon.
"""


from cse163_utils import Pokemon


# Your code here!
def species_count(data: list[Pokemon]) -> int:
    """
    This method takes in a dictionary of Pokemons. It counts the number of
    different species of Pokemon is in the file.
    """
    result = []
    for pokemon in data:
        if pokemon['name'] not in result:
            result.append(pokemon['name'])
    return len(result)


def max_level(data: list[Pokemon]) -> tuple[str, int]:
    """
    This method takes in a dictionary of Pokemons. It finds the Pokemon with
    the highest level and returns the name of the Pokemon, as well as
    the level.
    """
    selected = 0
    for pokemon in data:
        if pokemon['level'] > selected:
            selected = pokemon['level']
    for pokemon in data:
        if pokemon['level'] == selected:
            return (pokemon['name'], pokemon['level'])


def filter_range(data: list[Pokemon], range_min: int,
                 range_max: int) -> list[str]:
    """
    This method takes in a dictionary of Pokemons and the range of the level
    that we are trying to find. It returns a list of all the Pokemons
    that is in between the range that we want.
    """
    result = []
    for pokemon in data:
        if (pokemon['level'] < range_max) and (pokemon['level'] >= range_min):
            result.append(pokemon['name'])
    return result


def mean_attack_for_type(data: list[Pokemon], s: str) -> float | None:
    """
    This method takes in a dictionary of Pokemons and a string. The string
    is for the type of Pokemon and this method finds the average attack of
    Pokemons with the given type. In the case that there are no Pokemons of
    that type, it returns None.
    """
    result = []
    for pokemon in data:
        if pokemon['type'] == s:
            result.append(pokemon['atk'])
    if result == []:
        return None
    return sum(result) / len(result)


def count_types(data: list[Pokemon]) -> dict[str, int]:
    """
    This method takes in a dictionary of Pokemons. This programs
    counts the number of Pokemons in each type given in the dictionary,
    and it returns another dictionary with the names of the type as well as
    the number of Pokemons with that type.
    """
    result = {}
    for pokemon in data:
        if pokemon['type'] not in result:
            result[pokemon['type']] = 1
        else:
            result[pokemon['type']] += 1
    return result


def mean_attack_per_type(data: list[Pokemon]) -> dict[str, float]:
    """
    This method takes in a dictionary of Pokemons. This program lists
    the different types of Pokemon in the dictionary as well as the
    average attack of each of the types. It returns the result as another
    dictionary.
    """
    result = {}
    types = []
    for pokemon in data:
        if pokemon['type'] not in types:
            types.append(pokemon['type'])
    for t in types:
        result[t] = mean_attack_for_type(data, t)
    return result