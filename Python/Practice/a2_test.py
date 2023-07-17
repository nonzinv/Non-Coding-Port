"""
Non Pronanun
CSE 163 AD

This is the test file for a2.
"""


import a2

from cse163_utils import assert_equals


def test_total() -> None:
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, a2.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, a2.total(1))
    assert_equals(0, a2.total(0))

    # Test the None case
    assert_equals(None, a2.total(-1))


def test_travel() -> None:
    """
    Tests the travel method
    """
    assert_equals((-1, 4), a2.travel('NW!ewnW', (1, 2)))
    assert_equals((0, 3), a2.travel('NW!ewn', (1, 1)))
    assert_equals((2, 0), a2.travel('tree', (0, 0)))


def test_reformat_date() -> None:
    """
    Tests the reformate date method
    """
    assert_equals("31/12/1998", a2.reformat_date("12/31/1998", "M/D/Y",
                                                 "D/M/Y"))
    assert_equals("4/0", a2.reformat_date("0/200/4", "Y/D/M",
                                          "M/Y"))
    assert_equals("2", a2.reformat_date("3/2", "M/D", "D"))
    assert_equals("3/1/2", a2.reformat_date("1/2/3", "M/D/Y",
                                            "Y/M/D"))
    assert_equals("31/12", a2.reformat_date("12/31", "M/D", "D/M"))
    assert_equals("2/2023", a2.reformat_date("2023/2", "Y/M", "M/Y"))


def test_longest_word() -> None:
    """
    Tests the longest_word method
    """
    assert_equals('3: Merrily,', a2.longest_word('/home/song.txt'))
    assert_equals('1: corgis', a2.longest_word('/home/dog.txt'))
    assert_equals('11: testing....', a2.longest_word('/home/test.txt'))


def test_get_average_in_range() -> None:
    """
    Tests the get_average_in_range method
    """
    assert_equals(2.0666666, a2.get_average_in_range([1, 2, 3.2], -1, 10))
    assert_equals(5.5, a2.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2, a2.get_average_in_range([0, 2, 2, 4], 1, 3))
    assert_equals(3, a2.get_average_in_range([1, 2, 4, 6], 1.7, 5))


def test_mode_digit() -> None:
    """
    Tests the mode_digit method
    """
    assert_equals(2, a2.mode_digit(1211232231))
    assert_equals(1, a2.mode_digit(12121))
    assert_equals(0, a2.mode_digit(0))
    assert_equals(2, a2.mode_digit(-122))
    assert_equals(7, a2.mode_digit(77777776666666))
    assert_equals(3, a2.mode_digit(33333321))


def main():
    test_total()
    # Call your test functions here!
    test_travel()
    test_reformat_date()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == '__main__':
    main()