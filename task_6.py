while True:
    day = 1
    start = float(input("Введите начальный результат: "))
    finish = float(input("Введите конечный результат: "))
    if start <= 0 or finish <= 0:
        print("Введите корректные данные! Они должны быть больше 0.")
    else:
        while start < finish:
            start += start * 0.1
            day += 1
        print(f"Спортсмену удастся достгнуть рузьтата на {day}")



