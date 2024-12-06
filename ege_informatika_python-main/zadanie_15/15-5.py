'''
(А.М. Кабанов) Для какого наибольшего целого неотрицательного числа А выражение
(x**2 – 11x + 28 > 0) ∨ (y**2 – 9y + 14 > 0) ∨ (x**2 + y**2 > A)
тождественно истинно, т.е. принимает значение 1 при любых целых положительных x и y?
'''
def f(x, y, a):
    return (x ** 2 - 11 * x + 28 > 0) or (y ** 2 - 9 * y + 14 > 0) or (x ** 2 + y ** 2 > a)

for a in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not(f(x, y, a)):
                flag = False
                break
        if not(flag):
            break
    if flag:
        print(a)
