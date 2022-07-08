"""Ex06 - Dictionary Functions - Function Implementation"""
__author__ = """730462650"""


def invert(my_dict: dict[str, str]) -> dict[str, str]: 
    """Switches the key and value of a dictionary."""
    inverted_dict: dict[str, str] = dict() 
    for key in my_dict:
        if my_dict[key] in inverted_dict: 
            raise KeyError("Duplicate Keys")
        inverted_dict[my_dict[key]] = key
    return inverted_dict 


def favorite_color(my_dict: dict[str, str]) -> str: 
    """Returns the most common color from dictionary."""
    colors_output: dict[str, int] = dict()
    for key in my_dict: 
        if my_dict[key] in colors_output:
            colors_output[my_dict[key]] += 1
        else: 
            colors_output[my_dict[key]] = 1
    i: int = 0
    my_fave: str = ""
    for a in colors_output: 
        if colors_output[a] > i: 
            i = colors_output[a]
            my_fave = a
    return my_fave


def count(list: list[str]) -> dict[str,int]: 
    """Count of the number of times that value appeared in input list."""
    dictionary: dict[str, int] = dict()
    for k in list: 
        if k in dictionary: 
            dictionary[k] += 1
        else: 
            dictionary[k] = 1
    return dictionary 