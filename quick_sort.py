from partition import randomized_partition


def randomized_quick_sort(array: list, p: int, r: int) -> None:
    """
    This function implements randomized quick-sort. (As described in the university book).

    Parameters
    ----------
    array : list
        The array to sort.
    p : int
        The starting index of the array / sub-array.
    r : int
        The ending index of the array / sub-array.

    Notes
    -----

    The time complexity of this function in the average case is O(n*lg n).
    Worst case is O(n^2) but it is extremely rar.
    """
    if p < r:
        q = randomized_partition(array, p, r)
        randomized_quick_sort(array, p, q - 1)
        randomized_quick_sort(array, q + 1, r)



