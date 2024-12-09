from pair import *
import re

def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    return re.findall(r'[\d\.]+|\S{1}', expression)


# OPTIONAL
def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    if tokens[index] == '(':
        operator = tokens[index+1]
        if index != 0:
            rest1, index = parse_tokens(tokens, index+2)
            operator = Pair(operator, rest1)
        else:
            index += 2
        
        rest2, index = parse_tokens(tokens, index)

        pair = Pair(operator, rest2)

        return (pair, index)
    elif tokens[index] == ')':
        return (nil, index+1)
    else:
        try:
            n = 0
            if '.' in tokens[index]:
                n = float(tokens[index])
            else:
                n = int(tokens[index])
            
            rest, index = parse_tokens(tokens, index+1)
            pair = Pair(n, rest)

            return (pair, index)

        except:
            raise TypeError

