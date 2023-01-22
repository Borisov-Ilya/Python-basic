# Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод
# родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
# Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.

class Animal:
    num_of_insts = 0

    def __init__(self):
        Animal.num_of_insts += 1

    def voice(self):
        pass

    def print_num():
        print(Animal.num_of_insts)

    print_num = staticmethod(print_num)


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.__voice = 'Cat: meow'

    def voice(self):
        print(self.__voice)


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.__voice = 'woof'

    def voice(self):
        print(f"Dog: {self.__voice}!!!")


class Cow(Animal):
    def __init__(self):
        super().__init__()

    def voice(self):
        print('Cow: moo')


Animal.print_num()
cat = Cat()
Animal.print_num()
dog = Dog()
Animal.print_num()
cow = Cow()
Animal.print_num()
