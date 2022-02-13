a = int(input("Введите число целое положительное число: "))
big = 0
number = a

while number > 0:
    digit = number % 10
    if digit > big:
        big = digit
        if digit == 9:
            break
    number = number // 10
print(f"Наибольшая цифра в числе {a} это {big}")