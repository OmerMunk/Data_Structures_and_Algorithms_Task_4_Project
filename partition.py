from random import randint
from utils import swap
from utils import solution_2_add_compare


def partition(array: list, p: int, r: int):
    """
    This function implements partition.

    Parameters
    ----------

    array : list
        The array to execute the partition on.

    p : int
        The starting index of the array / sub-array.

    r: int
        The ending index of the array / sub-array.


    Returns
    -------

    `~i + 1`
        The pivot index, after all the elements are arranged by bigger or smaller than the pivot.

    Notes
    -----
    The time complexity of this function is O(n),
    n = r - p + 1.

    """
    x = array[r]
    i = p - 1
    for j in range(p, r):
        solution_2_add_compare()
        if array[j] <= x:
            i = i + 1
            swap(array, i, j)
    swap(array, i + 1, r)
    return i + 1


def randomized_partition(array, p, r) -> int:
    """
    This function implements randomized partition.
    It uses partition.

    Parameters
    ----------
    array : list
        The array to execute the randomized partition on.

    p : int
        The starting index of the array / sub-array.

    r: int
        The ending index of the array / sub-array.

    Returns
    -------
    `~partition(array, p, r)`
        The pivot index, after all the elements are arranged by bigger or smaller than the pivot.

    """
    i = randint(p, r)
    swap(array, r, i)
    return partition(array, p, r)
