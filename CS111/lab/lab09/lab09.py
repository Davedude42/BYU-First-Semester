import random


def in_range1(n):
    """Write a function that checks to see if n is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    "*** YOUR CODE HERE ***"

    if n > 0 and n <= 100:
        return True
    else:
        return False


def main():
    """Write code in the main function that generates 1000 
    random numbers between 1 and 101 and calls the generated 
    function to validate the number generated."""
    "*** YOUR CODE HERE ***"


def in_range2(n):
    """Redo in_range1, but throw an exception instead of 
    throwing false
    """
    "*** YOUR CODE HERE ***"
    if n > 0 and n <= 100:
        return None
    else:
        raise ValueError
