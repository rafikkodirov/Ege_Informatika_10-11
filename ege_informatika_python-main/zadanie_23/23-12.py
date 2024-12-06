'''
У исполнителя Калькулятор есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2
3. Умножить на 2
Сколько разных чисел на отрезке [34, 59] может быть получено из числа 1 с помощью программ, состоящих из 6 команд?
'''
s = set()
def f(x, k):
    global s
    if k == 6:
        s.add(x)
    else:
        f(x + 1, k + 1)
        f(x + 2, k + 1)
        f(x * 2, k + 1)

f(1, 0)
s1 = set([i for i in range(34, 60)])
print(len(s & s1))