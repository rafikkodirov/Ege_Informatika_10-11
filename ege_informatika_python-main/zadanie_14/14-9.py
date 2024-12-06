'''
(А. Кабанов) Значение выражения 125 ** 7 - 25 ** 4 + x записали в пятеричной системе счисления, при этом в записи оказалось 15
цифр 4, одна тройка и две единицы. При каком минимальном натуральном x это возможно?
'''
for x in range(1, 1000):
    f = 125 ** 7 - 25 ** 4 + x
    s = ''
    while f > 0:
        s += str(f % 5)
        f //= 5
    if s.count('4') == 15 and s.count('3') == 1 and s.count('1') == 2:
        print(x)
        break

