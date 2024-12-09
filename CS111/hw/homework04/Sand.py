from Particle import Particle

class Sand(Particle):


	def is_move_ok(self, x, y):
		if abs(x - self.x) <= 1 and y - self.y == 1 and x >= 0 and y >= 0 and x < self.grid.width and y < self.grid.height and self.grid.get(x, y) == None:
			# Diagonal check
			if x == self.x or self.grid.get(x, y - 1) == None:
				return True
		return False

	def physics(self):
		if self.is_move_ok(self.x, self.y + 1):
			return (self.x, self.y + 1)
		if self.is_move_ok(self.x - 1, self.y + 1):
			return (self.x - 1, self.y + 1)
		if self.is_move_ok(self.x + 1, self.y + 1):
			return (self.x + 1, self.y + 1)
		
		return None