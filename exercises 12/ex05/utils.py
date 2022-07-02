"""Ex05 - 'List' Utility Functions."""
__author__ = "730462650"


def only_evens(x: list[int]) -> list[int]:
    """Given a list, return only the even numbers."""
    evens: list[int] = list()
    for i in x: 
        if i % 2 == 0:
            evens.append(i)
    return evens


def is_equal(a: list[int], b: list[int]) -> bool:
    """Returns true if both all indexes in both lists are the same."""
    if len(a) == len(b):
        index: int = 0
        result: bool = True
        for i in a: 
            if i != b[index]:
                result = False
            index += 1
        return result
    return False


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Generates subset of given list."""
    result = []
    if b < 0: 
        b = 0 
    if c - 1 > len(a):
        c = len(a) - 1
    if len(a) == 0 or b > len(a) or c <= 0 or b == len(a):
        return []
    while b < c: 
        result.append(a[b])
        b += 1
    return result 