# Есть класс Animal c одним методом voice().
# class Animal:
# def voice(self):
# pass
# 1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
#
# 2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

class Animal:
    def voice(self):
        pass


class Cat(Animal):
    def __init__(self):
        self.__voice = 'Cat: meow'

    def voice(self):
        print(self.__voice)


class Dog(Animal):
    def __init__(self):
        self.__voice = 'woof'

    def voice(self):
        print(f"Dog: {self.__voice}!!!")


class Cow(Animal):
    def voice(self):
        print('Cow: moo')


cat = Cat()
dog = Dog()
cow = Cow()

cat.voice()
dog.voice()
cow.voice()
