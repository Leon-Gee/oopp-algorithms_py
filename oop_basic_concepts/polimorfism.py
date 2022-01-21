class Person:
    
    def __init__(self,name):
        self.name = name


    def move(self):
        print('walking')



class Ciclyst(Person):

    def __init__(self,name):
        super().__init__(name)


    def move(self):
        print('Moving on my bicycle')


if __name__ == '__main__':
    leon = Person('leon')
    leon.move()
    oscar = Ciclyst('oscar')
    oscar.move()
