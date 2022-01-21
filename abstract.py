
class Wash_machine:

	def __init__(self):
		pass


	def wash(self, temperature = 'hot'):
		self._fill_water_tank(temperature)
		self._add_soap()
		self._wash()
		self._dry()


	def _fill_water_tank(self, temperature):
		print(f'Filling the tank with {temperature} water')


	def _add_soap(self):
		print('adding soap')



	def _wash(self):
		print('Washing clothes')



	def _dry(self):
		print('drying clothes')




if __name__ == '__main__':
	washer = Wash_machine()

	washer.wash()
