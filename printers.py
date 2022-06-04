from math import floor, ceil

class Color:
    """
    This class holds properties of color printing strings.
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def printer(content=None, size=40):
    """
    This function is a styled printer function for displaying messages to the user.

    Parameters
    ----------
    content : str
        The content to print.

    size : int
        The amount of signs to print in each row around the content.
    """
    sign = '-'
    if not content:
        print(f"{Color.GREEN}{sign * size}{Color.END}\n")
    else:
        print(sign * size)  # Prints the first row
        # Prints the content, wrapped by the sings, to make sure that middle row will be in the same size of the rest
        print(f"{sign * floor((size - len(content)) / 2)}{content}{sign * ceil((size - len(content)) / 2)}")
        print(f"{sign * size}\n")  # Print the thrid and last row, then a new line
