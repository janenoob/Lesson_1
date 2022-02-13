a = int(input("Введите секунды: "))
hours = a // 3600
minutes = a % 3600 // 60
seconds = a % 60


print(f" {hours:02}:{minutes:02}:{seconds:02}")
