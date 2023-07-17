"""
Non Pronanun
CSE 163 AD

A file that has functions listed by the spec in Primer
"""


def total(n: int) -> int | None:
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result

# Write your functions here!


def travel(s: str, start: tuple[int, int]) -> tuple[int, int]:
    """
    Takes in a string and a tuple where the string will guide
    where the resulting tuple's coordinates are given in the string.
    If the input is not one of the letters corresponding to a direction,
    it is skipped and the case does not matter.
    """
    x_new = start[0]
    y_new = start[1]
    for i in s.lower():
        if i == 'n':
            y_new += 1
        if i == 's':
            y_new -= 1
        if i == 'w':
            x_new -= 1
        if i == 'e':
            x_new += 1
    return (x_new, y_new)


def reformat_date(date: str, curr_format: str, new_format: str) -> str:
    """
    It takes in a string for date with the current format and will
    transform this date into the desired format.
    """
    result = {}
    target = ''
    date = date.split('/')
    curr_format = curr_format.split('/')
    new_format = new_format.split('/')
    for i in range(len(curr_format)):
        result[curr_format[i]] = date[i]
    for i in range(len(new_format) - 1):
        target += result.get(new_format[i]) + '/'
    return target + result.get(new_format[len(new_format) - 1])


def longest_word(file_name: str) -> str | None:
    """
    This takes in a file and finds the longest word in the file
    and also which line containing the first occurrence. If there are
    2 words with the same length, it will return the one that occurs first.
    In the case that there are no words in the file, it will return None.
    """
    with open(file_name) as f:
        lines = f.readlines()
        if lines == []:
            return None
        longest = 0
        l_word = ''
        curr_line = 1
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) > longest:
                    longest = len(word)
                    l_word = str(curr_line) + ': ' + word
            curr_line += 1
    return l_word


def get_average_in_range(data: list[float], minn: float,
                         maxn: float) -> float:
    """
    Returns the average of a list that is passed in where it will
    only find the average for the items in the list within the given
    range. In the case that there are no values in the given range,
    it returns 0.
    """
    filtered = [i for i in data if i >= minn and i < maxn]
    if data == [] or filtered == []:
        return 0
    total = 0
    for i in filtered:
        total += i
    return total / len(filtered)


def mode_digit(n: int) -> int:
    """
    Takes in a integer, where it will find the number with the
    most occurrence in that integer. If two numbers have the
    same number of occurrence, the higher one is selected
    """
    result = {}
    n = abs(n)
    while n > 0:
        num = n % 10
        if num not in result:
            result[num] = 0
        result[num] += 1
        n = n // 10
    mode = int()
    counts = 0
    for i in result.keys():
        if result.get(i) >= counts:
            if i > mode:
                mode = i
            counts = result.get(i)
    return mode