from pair import Pair, nil
import re
from operator import add, sub, mul, truediv

def loop():

	txt = input("calc >> ")

	if txt == 'exit':
		return False
	try:
		tokens = tokenize(txt)
		pair = parse(tokens)
		result = eval(pair)
		print(result)
	except Exception as e:
		print(f"Error: {str(e)}")

	return True

def eval(syntax_tree):
	if isinstance(syntax_tree, int) or isinstance(syntax_tree, float):
		return syntax_tree
	elif isinstance(syntax_tree, Pair):
		if syntax_tree.rest is nil:
			return Pair(eval(syntax_tree.first), nil)
		
		syntax_tree.rest = eval(syntax_tree.rest)

		if isinstance(syntax_tree.first, str):
			operator = syntax_tree.first
			#print("About to apply", operator, repr(syntax_tree.rest))
			return apply(operator, syntax_tree.rest)
		else:
			syntax_tree.first = eval(syntax_tree.first)
			return syntax_tree
	else:
		raise TypeError(f"Not good syntax tree {syntax_tree}")

def reduce(func, operands, initial):
	res = initial
	while isinstance(res, Pair):
		res = res.first

	while operands is not nil:
		#print(res, operands.first, "gg")
		opp2 = operands.first
		while isinstance(opp2, Pair):
			opp2 = opp2.first
		res = func(res, opp2)
		operands = operands.rest

	return res
		

def apply(operator, operands):
	if operator == '+':
		return reduce(add, operands, 0)
	elif operator == '*':
		return reduce(mul, operands, 1)
	elif operator == '-':
		return reduce(sub, operands.rest, operands.first)
	elif operator == '/':
		return reduce(truediv, operands.rest, operands.first)
	
	raise TypeError
		

def parse(tokens):
	pair, _ = parse_tokens(tokens, 0)
	return pair
		 

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

def main():
	print("Welcome to the CS 111 Calculator Interpreter.")

	while loop():
		continue

	print("Goodbye!")

if __name__ == '__main__':
	main()
