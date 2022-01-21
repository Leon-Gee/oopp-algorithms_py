
class Coordinate:

	def __init__(self, x, y):
		self.x = x
		self.y = y


	def distance(self, point):
		x_diff = (self.x - point.x)**2
		y_diff = (self.y - point.y)**2

		return (x_diff + y_diff)**0.5


if __name__ == '__main__':
	coord1 = Coordinate(x = 3, y = 30)
	coord2 = Coordinate(x = 4, y = 8)

	print(coord1.distance(point = coord2))
