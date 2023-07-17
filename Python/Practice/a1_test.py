"""
Non Pronanun
CSE 163 AD

This file is used to test the functions of a1, given in the spec
"""


import a1

from cse163_utils import assert_equals


def test_total() -> None:
    """
    This function tests whether the behavior of the a1 functions are
    accurate according to the spec or not.
    """
    # The regular case
    assert_equals(15, a1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, a1.total(1))
    assert_equals(0, a1.total(0))
    # TODO: add your own total test here
    assert_equals(None, a1.total(-5))


def test_funky_sum() -> None:
    """
    This function tests whether the behavior of the funky_sum function are
    accurate according to the spec or not.
    """
    assert_equals(2.0, a1.funky_sum(1, 3, 0.5))
    assert_equals(1, a1.funky_sum(1, 3, 0))
    assert_equals(1.5, a1.funky_sum(1, 3, 0.25))
    assert_equals(2.2, a1.funky_sum(1, 3, 0.6))
    assert_equals(3, a1.funky_sum(1, 3, 1))
    assert_equals(2, a1.funky_sum(2, 2, 2))
    assert_equals(5, a1.funky_sum(5, 5, 5))


def test_swip_swap() -> None:
    """
    This function tests whether the behavior of the swip_swap function are
    accurate according to the spec or not.
    """
    assert_equals('offbar', a1.swip_swap('foobar', 'f', 'o'))
    assert_equals('dawgzzz', a1.swip_swap('dawgsss', 's', 'z'))
    assert_equals('ocrgis', a1.swip_swap('corgis', 'c', 'o'))
    assert_equals('corgis', a1.swip_swap('ocrgis', 'c', 'o'))
    assert_equals('valorant', a1.swip_swap('avlorvnt', 'v', 'a'))


def main():
    test_total()
    test_swip_swap()
    test_funky_sum()


if __name__ == '__main__':
    main()