# Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) и создать на его основе новый файл,
# где содержимое будет записано в обратном порядке.
# В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке.

str = '123\nqwerty'

with open('file_1.txt', 'w') as file_1:
    file_1.write(str)

with open('file_1.txt', 'r') as file_1:
    print(file_1.read())

print()

with open('file_2.txt', 'w') as file_2:
    file_2.write(str[::-1])

with open('file_2.txt', 'r') as file_2:
    print(file_2.read())
