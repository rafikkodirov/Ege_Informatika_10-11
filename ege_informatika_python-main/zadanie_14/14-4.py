'''
Значение арифметического выражения: 25 ** 56 + 5 ** 138 - 5 записали в системе счисления с основанием 5. Сколько цифр «4» в этой записи?
'''
x = 25 ** 56 + 5 ** 138 - 5
k = 0
while x > 0:
    if x % 5 == 4:
        k += 1
    x //= 5
print(k)