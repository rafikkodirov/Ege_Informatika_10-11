'''
Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
1. Перемножаются первая и вторая, а также вторая и третья цифры.
2. Полученные два числа записываются друг за другом в порядке неубывания без разделителей.
Пример. Исходное число: 631. Произведение: 6*3 = 18; 3*1 = 3. Результат: 318.
Укажите наибольшее число, при обработке которого автомат выдаёт результат 621.
'''
for x in range(100, 1000):
    s = str(x)
    summa1 = int(s[0]) * int(s[1])
    summa2 = int(s[1]) * int(s[2])
    if summa1 <= summa2:
        final = str(summa1) + str(summa2)
    else:
        final = str(summa2) + str(summa1)
    if final == '621':
        print(x)
