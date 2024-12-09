class Grid:
	"""
	2D grid with (x, y) int indexed internal storage
	Has .width .height size properties
	"""
	width = 0
	height = 0
	array = []

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.array = [[None for j in range(self.height)] for i in range(self.width)]

	def in_bounds(self, x, y):
		return x >= 0 and x < self.width and y >= 0 and y < self.height
	
	def get(self, x, y):
		if self.in_bounds(x, y):
			return self.array[x][y]
		else:
			raise IndexError(f"({x}, {y}) is out of range")
	
	def set(self, x, y, val):
		if self.in_bounds(x, y):
			self.array[x][y] = val
		else:
			raise IndexError(f"({x}, {y}) is out of range")

	def __str__(self):
		return f"Grid({self.height}, {self.width}, first = {self.get(0, 0)})"
	
	def __repr__(self):
		return f"Grid({self.height}, {self.width}, first = {self.get(0, 0)})"
	

	def __eq__(self, other):
		if isinstance(other, Grid):
			return self.array == other.array
		else:
			return False