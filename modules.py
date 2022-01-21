
class Vote_station:

	def __init__(self, uid, country):
		self.__uid = uid
		self.__country = country
		self.__region = None


	@property
	def region(self):
		return self.__region


	@region.setter
	def region(self, region):
		if region in self.__country:
			self.__region = region
		else:
			raise ValueError(f'The region {region} is not valid \
					\ {self.__country}')


if __name__ == '__main__':
	vote_station = Vote_station(123, ['sinaloa', 'culiacan'])
	vote_station.region = 'sinaloa'
	print(vote_station.region)
