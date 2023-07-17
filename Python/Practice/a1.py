"""
Non Pronanun
CSE 163 AD

This file contains the 3 functions given in the specs.
This includes funky_sum, total, and swip_swap.
"""


def funky_sum(a: float, b: float, mix: float) -> float:
    """
    This function takes in 3 float paramenters. If mix is less than 0,
    it returns a, and if mix is more than 1, it returns b. If mix is between
    1 and 0, then it calculates the appropriate weighted approximate.
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return ((1 - mix) * a) + (mix * b)


def total(n: int) -> int | None:
    """
    This function takes in an integer. If the integer is less than 0, it
    returns None. If the integer is more than 1, it returns the sum of ints
    from 1 inclusive of the value passed in.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(s: str, c1: str, c2: str) -> str:
    """
    This function takes in 3 strings. The first string is a word, and the
    rest should be letters. It swaps the letters passed in within the word.
    """
    s = list(s)
    result = ''
    for i in range(len(s)):
        if s[i] == c1:
            result += c2
        elif s[i] == c2:
            result += c1
        else:
            result += s[i]
    return result