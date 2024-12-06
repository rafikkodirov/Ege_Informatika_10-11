'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n*n + 2*n + 1, при n > 25
F(n) = 2*F(n+1) + F(n+3), при чётных n ≤ 25
F(n) = F(n+2) + 3*F(n+5), при нечётных n ≤ 25
Определите количество натуральных значений n из отрезка [1; 1000], для которых значение F(n) не содержит цифру 0.
'''
def f(n):
    if n > 25:
        return n * n + 2 * n  + 1
    else:
        if n % 2 == 0:
            return 2 * f(n + 1) + f(n + 3)
        else:
            return f(n + 2) + 3 * f(n + 5)

k = 0
for n in range(1, 1001):
    if '0' not in str(f(n)):
        k += 1
print(k)