'''
Автомат обрабатывает натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) Запись «переворачивается», то есть читается справа налево. Если при этом появляются ведущие нули, они отбрасываются.
3) Полученное число переводится в десятичную систему счисления и выводится на экран.
Какое наименьшее число, превышающее 100, после обработки автоматом даёт результат 9?
'''
for n in range(100, 1000):
    s = bin(n)[2:]
    if int(s[::-1], 2) == 9:
        print(n)
        break