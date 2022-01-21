
class Car:

	def __init__(self, model, brand, color):
		self.model = model
		self.brand = brand
		self.color = color
		self._state = 'resting'
		self.motor = Motor(cilinders = 4)


	def acelerate(self, type = 'gasoline'):
		if type == 'fast':
			self.motor.inyect_gasoline(quantity = 10)
		else:
			self.motor.inyect_gasoline(quantity = 3)

		self._state = 'in_movement'
		print(self._state)


class Motor:

	def __init__(self, cilinders, type = 'gasoline'):
		self.cilinders = cilinders
		self.type = type
		self._temperature = 0

	def inyect_gasoline(self, quantity):
		print('brrrrr')


if __name__ == '__main__':
	honda = Car('civic', 'honda', 'navy_blue')
	honda.acelerate(type = 'fast')
