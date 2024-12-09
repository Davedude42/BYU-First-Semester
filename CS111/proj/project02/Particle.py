

class Particle:
	grid = None
	x = 0
	y = 0

	def __init__(self, grid, x=0, y=0):
		self.grid = grid
		self.x = x
		self.y = y
	
	def __str__(self):
		return f"{type(self).__name__}({self.x},{self.y})"

	def move(self):
		movement = self.physics()

		if movement == None:
			return
		
		new_x, new_y = movement

		self.grid.set(self.x, self.y, None)
		self.x = new_x
		self.y = new_y
		self.grid.set(new_x, new_y, self)

	def physics(self):
		pass