def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [n*i for i, n in enumerate(s) if i % 2 == 0]


def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"

    return [[s[i], t[i]] for i in range(len(s))]

def count_appearances(lst):
    """Returns a dictionary containing each integer's appearance count
    >>> lst = [0]
    >>> count_appearances(lst)
    {0: 1}
    >>> lst = [0, 0, 1, 2, 1, 1]
    >>> count_appearances(lst)
    {0: 2, 1: 3, 2: 1}
    >>> lst = [0, 0, 0, 0, 0, 3, 0, 0]
    >>> count_appearances(lst)
    {0: 7, 3: 1}
    """
    "*** YOUR CODE HERE ***"
    ret = {}

    for n in lst:
        if n in ret:
            ret[n] += 1
        else:
            ret[n] = 1

    return ret

def copy_file(input_filename, output_filename):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    "*** YOUR CODE HERE ***"
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    formattedLines = []

    for i, l in enumerate(lines):
        formattedLines.append(f'{i + 1}: {l}')
        print(formattedLines[i], end="")

    with open(output_filename, 'w') as file:
        file.writelines(formattedLines)

########################################################
# OPTIONAL QUESTIONS


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """

    return [i for i in range(1, n) if n % i == 0]


def slice_and_multiplice(lst):
    """Return a new list where all values past the first are
    multiplied by the first value.

    >>> slice_and_multiplice([1,1,6])
    [1, 6]
    >>> slice_and_multiplice([9,1,5,2])
    [9, 45, 18]
    >>> slice_and_multiplice([4])
    []
    >>> slice_and_multiplice([0,4,9,18,20])
    [0, 0, 0, 0]
    """
    # Write your code here

    return [lst[i] * lst[0] for i in range(1, len(lst))]