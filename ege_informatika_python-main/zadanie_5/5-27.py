'''
Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные двузначные числа (числа не могут начинаться с нуля).
2. На экран выводится разность полученных двузначных чисел.
Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53, наименьшее – 13. На экран выводится разность 53 – 13 = 40.
Чему равно количество чисел N на отрезке [300; 400], в результате обработки которых на экране автомата появится число 20?
'''
k = 0
for n in range(300, 401):
    s = sorted(str(n))
    if s[0] == '0':
        if s[1] == '0':
            minimum = maximum = int(s[2] + '0')
        else:
            minimum = int(s[1] + '0')
            maximum = int(s[2] + s[1])
    else:
        minimum = int(s[0] + s[1])
        maximum = int(s[2] + s[1])
    if maximum - minimum == 20:
        k += 1
print(k)