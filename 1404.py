class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print('Som genérico de animal')

class dog(animal):
    def sound(self):
        print('Au Au!')

class cat(animal):
    def sound(self):
        print('Miau!')