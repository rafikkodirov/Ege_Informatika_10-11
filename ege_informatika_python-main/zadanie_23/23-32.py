'''
Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Умножить на 3
Программа для исполнителя Калькулятор – это последовательность команд. Сколько существует программ, для которых
при исходном числе 2 результатом является число 31, и при этом траектория вычислений не содержит число 25?
'''
def f(x, y):
    if x > y or x == 25:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

print(f(2, 31))