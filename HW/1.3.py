## 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
## должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
## числа используйте код:

from random import randint
num = randint(0, 1000) 
a = int(input("Введите число: "))
i = 1
print(num)
while i <= 5:
    if a > num:
        print("Меньше")
        i += 1
        a = int(input("Введите число: "))
    elif a < num:
        print("Больше")
        i += 1
        a = int(input("Введите число: "))
    elif a == num:
        print("Вы угадали число")
        break

    