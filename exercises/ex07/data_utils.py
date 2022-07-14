"""Dictionary related utility functions."""


__author__ = "730462650"


"""Some helpful utility funtions for working with CSV files."""


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a cdv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
    return result 


def head(my_dict: dict[str, list[str]], x: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first N rows of data for each column."""
    output: dict[str, list[str]] = {}
    for column in my_dict: 
        output[column] = []
        i: int = 0 
        while i < x and i < len(my_dict[column]): 
            output[column].append(my_dict[column][i])
            i += 1
    return output


def select(my_dict: dict[str, list[str]], x: list[str]) -> dict[str, list[str]]:
    """Makes a new column-based table with only a specific subset of original columns."""
    output: dict[str, list[str]] = {}
    for column in x: 
        output[column] = my_dict[column]
    return output


def concat(dictionary1: dict[str, list[str]], dictionary2: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Combines two column-based tables."""
    output: dict[str, list[str]] = {}
    for column in dictionary1: 
        output[column] = dictionary1[column]
    for column2 in dictionary2: 
        if column2 in output:
            output[column2] = dictionary1[column2] + dictionary2[column2]
        else: 
            output[column2] = dictionary2[column2]
    return output


def count(x: list[str]) -> dict[str, int]:
    """Counts the number of times a key has appeared in an input list."""
    output: dict[str, int] = {}
    for item in x:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1
    return output