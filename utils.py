import random
import sys


def swap(array: list, i: int, j: int) -> None:
    """
    This function receives two indexes of an array, and swaps the values in those indexes.

    Parameters
    ----------

    array : list
        An array to swap the two values in.
    i : int
        The index of the first value.
    j : int
        The index of the second value.

    Notes
    -----
    Time complexity of this function is O(1).
    """
    temp = array[i]  # Storing the first value in a temporary variable
    array[i] = array[j]
    array[j] = temp


def generate_array(amount: int) -> list:
    """
    This function generates an array with the length of the given amount, and random values from 0 to 999.

    Parameters
    ----------
    amount: int
        the desired length of the array to generate.

    Returns
    -------
    `~array`
        The generated Array.

    Notes
    -----
    Time complexity of this function is O(n), n= amount.

    """
    array = []  # Creating an empty list
    for i in range(amount):
        array.append(random.randrange(0, 1000, 1))
        # Randrange generates random number between 0 and 999 with steps of 1
    return array


# Global variables that will be used to count the amount of compares that each solution does.
solution_1_compares = 0
solution_2_compares = 0


def solution_1_add_compare() -> None:
    """
    This function adds 1 to solution 1 compares count.
    """
    global solution_1_compares
    solution_1_compares += 1


def solution_2_add_compare() -> None:
    """
    This function adds 1 to solution 2 compares count.
    """
    global solution_2_compares
    solution_2_compares += 1


def get_solution_1_compares() -> int:
    """
    This function returns the current compares count of solution 1.

    Returns
    -------
    `~solution_1_compares`
        solution 1 compares count.
    """
    return solution_1_compares


def get_solution_2_compares() -> int:
    """
    This function returns the current compares count of solution 2.

    Returns
    -------
    `~solution_2_compares`
        Solution 2 compares count.
    """
    return solution_2_compares


def reset_solution_1_compares() -> None:
    """
    This function resets the compares count of solution 1 to 0.
    """
    global solution_1_compares
    solution_1_compares = 0


def reset_solution_2_compares() -> None:
    """
    This function resets the compares count of solution 2 to 0.
    """
    global solution_2_compares
    solution_2_compares = 0


