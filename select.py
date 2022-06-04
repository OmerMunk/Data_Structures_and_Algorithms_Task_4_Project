from partition import randomized_partition


def randomized_select(array: list, p: int, r: int, i: int):
    """
    This function implements Randomized-Select, and finds the k-smallest number of an array.
    It uses randomized partition

    Parameters
    ----------

    array : list
        An array to execute the randomized select on.

    p : int
        The starting index of the array / sub-array.

    r : int
        The ending index of the array / sub-array.

    i : int
        The target to find the i-smallest number of the array.

    Notes
    -----

    The time complexity of this function is O(n).

    """
    if p == r:
        return array[p]
    q = randomized_partition(array, p, r)
    k = q - p + 1
    if i == k:
        return array[q]
    elif i < k:
        return randomized_select(array, p, q - 1, i)
    else:
        return randomized_select(array, q + 1, r, i - k)

