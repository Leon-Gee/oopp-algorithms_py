
class Rectangle:

	def __init__(self, base, height):
		self.base = base
		self.height = height


	def area(self):
		return self.base * self.height



class Square(Rectangle):

	def __init__(self, side):
		super().__init__(side, side)


if __name__ == '__main__':

	rectangle = Rectangle(base=3, height=10)

	square = Square(side=3)

	print(rectangle.area())
	print(square.area())
