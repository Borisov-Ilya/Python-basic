# Вывести на экран сумму четных чисел от 1 до 100 включительно, используя функцию range()

result = 0

for x in range(1, 101):
    if x % 2 == 0:
        result += x

print(result)
