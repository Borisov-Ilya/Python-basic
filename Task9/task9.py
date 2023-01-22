# Необходимо создать два параллельных потока, каждый из которых выводил бы на экран числа от 10 до 1 в обратном
# порядке с интервалом в одну секунду.
# В выводе должно быть понятно какая нить выполняется, и когда каждая из них начинает и заканчивает своё выполнение.

import threading
import time


def thread_1():
    print('Поток 1 - старт')

    for i in range(10, 0, -1):
        print(f"Поток 1 - {i}")
        time.sleep(1)

    print('Поток 1 - финиш')


def thread_2():
    print('Поток 1 - старт')

    for i in range(10, 0, -1):
        print(f"Поток 2 - {i}")
        time.sleep(1)

    print('Поток 2 - финиш')


t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)


t1.start()
t2.start()
