from copy import deepcopy

class Grid:
	"""
	2D grid with (x, y) int indexed internal storage
	Has .width .height size properties
	"""
	width = 0
	height = 0
	array = []

	@staticmethod
	def check_list_malformed(lst):
		if not isinstance(lst, list):
			raise ValueError("Not a list")
		if len(lst) == 0:
			raise ValueError("Empty list") 
		if not isinstance(lst[0], list):
			raise ValueError("Sublist not list")
		
		l = len(lst[0])
	
		for i in range(len(lst)):
			if not isinstance(lst[0], list):
				raise ValueError("Sublist not list")
			if len(lst[i]) != l or len(lst[i]) == 0:
				raise ValueError("Mismatched list size")
			
	@staticmethod
	def build(lst):
		Grid.check_list_malformed(lst)

		grid = Grid(len(lst[0]), len(lst))
		grid.array = deepcopy(lst)

		return grid
		

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.array = [[None for j in range(self.width)] for i in range(self.height)]

	def in_bounds(self, x, y):
		return x >= 0 and x < self.width and y >= 0 and y < self.height
	
	def get(self, x, y):
		if self.in_bounds(x, y):
			return self.array[y][x]
		else:
			raise IndexError(f"({x}, {y}) is out of range")
	
	def set(self, x, y, val):
		if self.in_bounds(x, y):
			self.array[y][x] = val
		else:
			raise IndexError(f"({x}, {y}) is out of range")

	def __str__(self):
		return f"Grid({self.height}, {self.width}, first = {self.get(0, 0)})"
	
	def __repr__(self):
		return f"Grid.build({self.array})"
	

	def __eq__(self, other):
		if isinstance(other, Grid):
			return self.array == other.array
		elif isinstance(other, list):
			return self.array == other
		else:
			return False
		
	def copy(self):
		grid = Grid(self.width, self.height)
		grid.array = deepcopy(self.array)

		return grid
	

	