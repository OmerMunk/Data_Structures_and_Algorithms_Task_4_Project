import sys
from math import floor, log2, ceil
from utils import swap
from utils import solution_1_add_compare


class Heap:
    """
    Heap is a class the implements the structure and the methods of a minimum-heap.
    """

    def __init__(self, max_size: int, array: list = None):
        """
        A constructor for the Heap class.

        Parameters
        ----------
        max_size : int
            the maximum size of the array the contains the heap.
        array : list
            an optional parameter, if given, than it creates the heap with the values of the given array.
        """
        if array:
            self.max_size = len(array) - 1
            self.heap_size = len(array)
            self.heap = array
            # inserts the minimum size of integer to the '0' index, to make the code more readable and reasonable.
            self.heap.insert(0, -sys.maxsize)
        else:
            self.heap_size = 0
            self.max_size = max_size
            self.heap = [None] * (self.max_size + 1)
            # sets the value of index '0' to the minimum size of integer ,
            # to make the code more readable and reasonable.
            self.heap[0] = -sys.maxsize

    @staticmethod
    def parent(i):
        """
        This function returns the parent's index of the index that was given as a parameter.

        Parameters
        ----------
        i : int
            The index to return its parent's index.

        Returns
        -------

        '~floor(i / 2)'
            The parent's index of the index that was given as a parameter.
        """
        return floor(i / 2)

    @staticmethod
    def left(i):
        """
        This function returns the left child's index of the index that was given as a parameter.

        Parameters
        ----------
        i : int
            The index to return its left child's index.

        Returns
        -------

        '~floor(i / 2)'
            The left child's index of the index that was given as a parameter.
        """
        return 2 * i

    @staticmethod
    def right(i):
        """
        This function returns the right child's index of the index that was given as a parameter.

        Parameters
        ----------
        i : int
            The index to return its right child's index.

        Returns
        -------

        '~floor(i / 2)'
            The right child's index of the index that was given as a parameter.
        """
        return 2 * i + 1

    def amount_of_elements(self):
        """
        This function returns the size of the heap.

        Returns
        -------

        `~self.heap_size`
            The size of the heap
        """
        # the possible amount of elements in heap that has a size H is:
        # 2^H <= amount <= 2^H+1 -1
        return self.heap_size

    def height(self):
        """
        This function returns the height of the heap.

        Returns
        -------

        `~floor(log2(self.amount_of_elements()))`
            The height of the heap (as an almost whole binary tree).
        """
        # the possible range is: height = floor(log(amount)) = Theta(n)
        return floor(log2(self.amount_of_elements()))

    @staticmethod
    def indexes_of_leaves(amount: int) -> None:
        """
        This function prints the possible indexes of the leaves (as an almost whole binary tree).
        """
        print(f"The leaves are between the indexes: {floor(amount / 2 + 1)} and {amount}")

    def amount_of_leaves(self):
        """
        This function returns the amount of leaves in the heap (as an almost whole binary tree).

        Returns
        -------
        `~ceil(self.amount_of_elements() / 2)`
            The amount of leaves in the heap.
        """
        return ceil(self.amount_of_elements() / 2)

    def amount_of_inner_nodes(self):
        """
        This function returns the amount of inner nodes (as an almost whole binary tree)

        Returns
        -------
        `~floor(self.amount_of_elements() / 2)`
            The amount of the inner nodes
        """
        return floor(self.amount_of_elements() / 2)

    def heapify_down(self, i: int) -> None:
        """
        This function implements heapify-down, it gets an index, and 'slides-down' the element in that index to its
        correct place of the heap hierarchy

        Parameters
        ----------

        i : int
            The index of the element to heapify down.
        """
        left_child = self.left(i)
        right_child = self.right(i)
        smallest = i

        if left_child <= self.heap_size:
            solution_1_add_compare()  # Counting the compares of solution1
            if self.heap[left_child] < self.heap[i]:
                smallest = left_child

        if right_child <= self.heap_size:
            solution_1_add_compare()  # Counting the compares of solution1
            if self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
        if smallest != i:
            swap(self.heap, i, smallest)
            self.heapify_down(smallest)

    def heapify_up(self, i: int) -> None:
        """
        This function implements heapify-up, it 'slides-up' an element in the given index to its correct place in the
        hierarchy of the heap.

        Parameters
        ----------

        i : int
            The index of the element to heapify up.

        """
        parent = self.parent(i)
        smallest = i
        solution_1_add_compare()  # Counting the compares of solution1
        if self.heap[parent] > self.heap[i]:
            smallest = parent
        if smallest != i:
            swap(self.heap, i, parent)
            self.heapify_up(parent)

    def heap_extract_min(self) -> int:
        """
        This function extracts the minimum value of the min-heap and then arranges it to still meet the requirements
        for a min-heap.

        Returns
        -------

        `~minimum`
            The minimum value of the min-heap

        Notes
        -----

        The time complexity of this function is O(lg n)
        """
        if self.heap_size < 1:
            raise Exception("heap underflow")
        minimum = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap.pop(self.heap_size)
        self.heap_size = self.heap_size - 1
        self.heapify_down(1)
        return minimum

    def heap_insert(self, value: int) -> None:
        """
        This function inserts a value to the end of the heap, and then uses heapify-up to place the new value in the
        correct place.

        Parameters
        ----------
        value : int
            The new value to insert to the heap.
        """
        self.heap_size = self.heap_size + 1
        self.heap[self.heap_size - 1] = value
        self.heapify_up(self.heap_size - 1)

    @staticmethod
    def build_heap(array: list):
        """
        This function build a minimum-heap using heapify down on the given array.

        Parameters
        ----------

        array : list
            the array to build the min-heap with.

        Returns
        -------
        `~heap`
            The min-heap that was created with the given array.

        Notes
        -----
        The time complexity of this function is O(n).
        """
        heap = Heap(len(array), array)
        for i in range(floor(heap.heap_size / 2), 0, -1):
            heap.heapify_down(i)
        return heap
