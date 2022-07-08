"""Ex06 - Dictionary Functions - Test."""
__author__ = "730462650"


from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert_number_one() -> None: 
    """USE- First test to switch the value and key of my dictionary."""
    my_dict: dict = {'H&M': 'Shop', 'Taco Bell': 'Food', 'Walmart': 'Store'}
    assert invert(my_dict) == {'Shop': 'H&M', 'Food': 'Taco Bell', 'Store': 'Walmart'}


def test_invert_number_two() -> None: 
    """USE- Second test to switch the value and key of my dictionary."""
    my_dict: dict = {'A': 'Number One', 'C': 'Number Two', 'B': 'Number Three'}
    assert invert(my_dict) == {'Number One': 'A', 'Number Two': 'C', 'Number Three': 'B'}


def test_invert_number_three() -> None: 
    """EDGE- Third test to switch the value and key of my dictionary."""
    my_dict: dict = {'Water': 'Bottle'}
    assert invert(my_dict) == {'Bottle': 'Water'}


def test_favorite_color_one() -> None: 
    """USE- First test to find most common color."""
    my_dict: dict = {'Bob': 'Yellow', 'Martha': 'Red', 'Tina:': 'Red', 'Harry': 'Blue'}
    assert favorite_color(my_dict) == 'Red'


def test_favorite_color_two() -> None: 
    """USE- Second test to find most common color."""
    my_dict: dict = {'Sarah': 'Blue', 'Tom': 'Purple', 'Betsy': 'White', 'Jared': 'Blue'}
    assert favorite_color(my_dict) == 'Blue'


def test_favorite_color_three() -> None: 
    """EDGE- Third test to find most common color."""
    my_dict: dict = {'Long': 'Term', 'Short': 'Term', 'Water': 'Bottle'}
    assert favorite_color(my_dict) == 'Term'


def test_count_one() -> None: 
    """USE- First test to return value frequency."""
    my_dict: dict = {'zero', 'one', 'zero', 'zero', 'one'}
    assert count(my_dict) == {'zero': 3, 'one': 2}


def test_count_two() -> None: 
    """USE- Second test to return value frequency."""
    my_dict: dict = {'yes', 'yes', 'no', 'no'}
    assert count(my_dict) == {'yes': 2, 'no': 2}


def test_count_three() -> None: 
    """EDGE- Third test to return value frequency."""
    my_dict: dict = {'what', 'is', 'your', 'name'}
    assert count(my_dict) == {'what': 1, 'is': 1, 'your': 1, 'name': 1}