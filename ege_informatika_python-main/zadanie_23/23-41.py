'''
Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:
1. Прибавь 1
2. Умножь на 2 и вычти 3
Сколько различных результатов можно получить из исходного числа 3 после выполнения программы, содержащей ровно 12 команд?

'''
s = set()
def f(x, k):
    global s
    if k == 12:
        s.add(x)
    else:
        f(x + 1, k + 1)
        f(x * 2 - 3, k + 1)

f(3, 0)
print(len(s))