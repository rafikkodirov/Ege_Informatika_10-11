"""
(В.Н. Шубинкин) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
Для какого наибольшего натурального числа A формула
((ДЕЛ(x, 36) ∧ ДЕЛ(x, 42)) → ДЕЛ(x, A)) ∧ ( A·(A – 25) < 25·(A + 200))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
"""
def f(x, a):
    return (((x % 36 == 0) and (x % 42 == 0)) <= (x % a == 0)) and (a *(a - 25) < 25 * (a + 200))

for a in range(1, 1000):
    answer = True
    for x in range(1, 1000):
        if not(f(x, a)):
            answer = False
            break
    if answer:
        print(a)