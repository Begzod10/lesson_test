from lesson.python_lessons import *


class Person:
    def __init__(self, name):
        self.name = name

    def run(self, surname):
        print(f'{surname}')

    def hello(self):
        print(f'Hello {self.name}')


hello()
