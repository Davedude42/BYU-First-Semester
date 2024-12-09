import sys


def print_args(args):
	for a in args:
		print(a)


def valid_args(args):
	if len(args) < 2:
		return False
	return args[1] == '-p' or args[1] == '-i' or args[1] == '-h' or args[1] == '-w' or args[1] == '-r'


def flags(args):
	if args[1] == '-p':
		print_args(args[2:])
	elif args[1] == '-i':
		print("Hello World")
	elif args[1] == '-h':
		print("Valid flags:\n-p : prints out all the command line arguments after the -p\n-i : prints \"Hello World\"\n-h : prints out a help command")
	elif args[1] == '-w':
		if len(args) <= 3:
			print("No Content Provided")
		else:
			with open(args[2], 'w') as file:
				for a in args[3:]:
					file.write(a + '\n')
	elif args[1] == '-r':
		with open(args[2], 'r') as file:
			lines = file.readlines()
			for l in lines:
				print(l, end='')
			print()


def main():
	if valid_args(sys.argv):
		flags(sys.argv)
	else:
		print_args(sys.argv)


main()