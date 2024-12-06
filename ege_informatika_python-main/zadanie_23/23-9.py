'''
Исполнитель Июнь17 преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 1
2. Сделай нечётное
Выполняя первую команду, исполнитель увеличивает число на 1, а выполняя вторую – из числа x получает число 2x+1.
Сколько существует программ, для которых при исходном числе 1 результатом является число 31 и при этом траектория вычислений не содержит число 25?
'''
def f(x, y):
    if x > y or x == 25:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(2 * x + 1, y)
print(f(1, 31))
