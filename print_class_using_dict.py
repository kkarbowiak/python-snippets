class Entity(object):
    def __init__(self):
        self.value1 = 'value1'
        self.value2 = 2
        self.value3 = [4, 5, 6]

    def __str__(self):
        return 'Entity is v1: {value1}, v2: {value2}, v3: {value3}'.format(**self.__dict__)

entity = Entity()
print(entity)
