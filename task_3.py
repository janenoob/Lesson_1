number = input("Ввведите число: ")
while number < '0':
    print("Ошибка! Введите число больше 0: ")
    number = input("Ввведите число: ")
print(f"{number} + {number+number} + {number+number+number} = {int(number) + int(number + number) + int(number + number + number)}")