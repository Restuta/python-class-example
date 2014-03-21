root_url = 'http://localhost:31337/'

class Person:
    legs = 4

    def __init__(self, legs_count):
        self.legs = legs_count

    def walk(self):
        print('walked with ' + str(self.legs) + ' legs')

#^^^^^^
#class and instance: person = Person()