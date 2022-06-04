from Heap import Heap
from quick_sort import randomized_quick_sort
from select import randomized_select
from utils import generate_array, get_solution_1_compares, get_solution_2_compares, reset_solution_1_compares, \
    reset_solution_2_compares

# Importing the function deepcopy, which can copy an array and all its elements to new places in the memory
# Contributes to the workflow of the project, i could have used simple copy using a for loop that copy each element,
# but it isn't what the project about. Copy is a built-in python package
from copy import deepcopy
from printers import printer, Color

# Importing matplotlib.pyplot, which is an external package use for plotting in python.
import matplotlib.pyplot as plt



def solution1(array, k, test=False):
    """
    This function executes the first solution to the problem: given an input of array with n elements, and k(positive
    integer), provide an output of the smallest k numbers. This solution build a minimum heap using the function
    build_min_heap from Heap.py, and then executes heap_extract_min from Heap.py,  k times in order the get the
    smallest k numbers.

    Parameters
    ----------

    array : list
        The array to build the heap with (must contain integers only).

    k : int
        k will signify the target amount for the smallest k numbers from the array to find.

    test : bool
        A configuration parameter, if True, then no additional ust prints will be executed except from the logic.
        If False, prints all the user messages and information.
    """
    heap1 = Heap.build_heap(array)  # Builds a minimum heap using the given array.
    output = [None] * k  # Creating an empty array of size k, to store the smallest k numbers of the output in it.
    for i in range(0, k):
        # Extracts the minimum number, while keeping the heap arranged as it should.
        smallest = heap1.heap_extract_min()
        output[i] = smallest  # Storing the smallest k numbers in the output array.
    if not test:  # The additional prints for the user if test mode is False.
        print(f"{Color.YELLOW}Results:{Color.END}\nthe k smallest number are: {output}\n")


def solution2(array, k, test=False):
    """
    This function executes the second solution to the problem: given an input of array with n elements,
    and k(positive integer), provide an output of the smallest k numbers. This solution runs randomized_select from
    select.py, in order to find the k-smallest number of the given array. And then sorting the smallest k numbers
    using quick_sort from quick_sort.py.

    Parameters
    ----------

    array : list
        The array to build the heap with (must contain integers only).

    k : int
        k will signify the target amount for the smallest k numbers from the array to find.

    test : bool
        A configuration parameter, if True, then no additional ust prints will be executed except from the logic.
        If False, prints all the user messages and information.
    """
    # Finding the k smallest number and arranging the whole array around him as the pivot element
    randomized_select(array, 0, len(array) - 1, k)
    randomized_quick_sort(array, 0, k - 1)  # Sorting the smallest k numbers
    if not test:  # The additional prints for the user if test mode is False.
        print(f"{Color.YELLOW}Results:{Color.END}\nthe k smallest number are: {array[0:k]}\n")


def statistical_test():
    """
    This is a statistical test, that executes the comparison between that two solution, about 2000 times,
    checks in each comparison which solution had the least compares, and draw a 3d scatter and bar plot that will
    demonstrate the difference between the amount of compares each solution does.

    """
    fig = plt.figure(figsize=(20, 20))  # Creating the plot figure
    ax = fig.add_subplot(111, projection='3d')  # Adding the 3rd axis ('z')

    # Setting the labels of each axis
    ax.set_xlabel("Length of array")
    ax.set_ylabel("k smallest")
    ax.set_zlabel("amount of compares")

    # Defining some values for the lengths of the arrays that will be automatically generated.
    lengths = [x for x in range(1000, 10001, 100)]

    # Defining some k values for the fins smallest k solutions.
    some_k = [x for x in range(50, 1000, 45)]

    print(f"Running {len(lengths) * len(some_k)} tests, for lengths from 1,000 to 10,000 with steps of 100,\nAnd for "
          f"k's from 50 to 999 with steps of 45")

    # Defining two empty arrays to store the amount of compares in each run of the solutions.
    solution1_compares = []
    solution2_compares = []

    for length in lengths:
        array1 = generate_array(length)  # generate a new array according to the current length.
        array2 = deepcopy(array1)  # Create an identical array but stored in a different place in the memory.
        for k in some_k:
            # Resets the compares count.
            reset_solution_1_compares()
            reset_solution_2_compares()

            # Running the two solutions.
            solution1(deepcopy(array1), k, test=True)
            solution2(deepcopy(array2), k, test=True)

            # Plotting the points according to the current results.
            ax.scatter(len(array1), k, get_solution_1_compares(), c='red')
            ax.scatter(len(array1), k, get_solution_2_compares(), c='blue')

            # Plotting the bars according to the current results.
            ax.bar3d(len(array1) + 10, k + 10, 0, -10, -10, get_solution_1_compares(), color='red')
            ax.bar3d(len(array1) - 10, k - 10, 0, 10, 10, get_solution_2_compares(), color='blue')

            # Stores the amount of compares of each solution.
            solution1_compares.append(get_solution_1_compares())
            solution2_compares.append(get_solution_2_compares())
    print(f"The average compares amount of solution 1 is: {sum(solution1_compares) / len(solution1_compares)}\n")
    print(f"The average compares amount of solution 2 is: {sum(solution2_compares) / len(solution2_compares)}\n")
    solution1_had_less_compares = 0
    solution2_had_less_compares = 0
    tie = 0
    for i in range(len(solution1_compares)):
        if solution1_compares[i] > solution2_compares[i]:
            solution2_had_less_compares += 1
        elif solution1_compares[i] < solution2_compares[i]:
            solution1_had_less_compares += 1
        else:
            tie += 1
    print(
        f"{Color.UNDERLINE}Solution 1 had less compares {solution1_had_less_compares} of the"
        f" {len(lengths) * len(some_k)} times.\nSolution 2 "
        f"had less compares {solution2_had_less_compares} of the {len(lengths) * len(some_k)} times\nTie was occurred"
        f" {tie} times")
    plt.show()  # Displays the results graph to the user
    plt.savefig('test_results1.png')  # Saves the plot as a file


if __name__ == "__main__":
    print(f"{Color.BLUE}Starting Project{Color.END}")

    valid = False
    n = input("please insert the length of the array:\t")
    while not valid:
        try:
            n = int(n)
            valid = True
        except ValueError as ex:
            print(ex)
            n = input('invalid input, please type an integer:\t')

    valid = False
    k = input("please insert the k:\t")
    while not valid:
        try:
            k = int(k)
            valid = True
        except ValueError as ex:
            print(ex)
            k = input('invalid input, please type an integer:\t')

    choice = input(
        "would you like to generate the values of the array? or choose them yourself?\nchoose g for generate, "
        "y for yourself:\t")
    while choice != "g" and choice != "y":
        print('invalid input, try again:\t')
        choice = input(
            "would you like to generate the values of the array? or choose them yourself?\nchoose g for generate, "
            "y for yourself:\t")

    if choice == "g":
        array1 = generate_array(n)
    else:
        array1 = []
        for i in range(0, n):
            valid = False
            value = input(f"please enter the {i + 1} out of {n} element of the array")
            while not valid:
                try:
                    value = int(value)
                    valid = True
                except ValueError as ex:
                    print(ex)
                    value = input('invalid input, please type a number')
            array1.append(value)

    array2 = deepcopy(array1)
    printer("starting test1")
    solution1(array1, k)
    printer(f"finished test1, took {get_solution_1_compares()} compares")
    printer()
    printer("starting test2")
    solution2(array2, k)
    printer(f"finished test2, took {get_solution_2_compares()} compares")
    statistical_test()
    print(f"{Color.RED}Finished Program{Color.END}")
