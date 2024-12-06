'''
168)	(А. Кабанов) Обозначим через S сумму всех натуральных делителей целого числа, кроме единицы и самого числа.
Если таких делителей у числа нет, то считаем значение S равным нулю. Напишите программу, которая перебирает целые числа,
большие 150000 в порядке возрастания и ищет среди них такие, для которых значение S при делении на 13 даёт остаток 10.
Программа должна найти и первые 7 таких чисел. Для каждого из них запишите в отдельной строке сначала само число, затем
значение S. Строки выводятся в порядке возрастания найденных чисел.
'''
for i in range(150000, 155000):
    divs = set()
    for d in range(2, round(i ** 0.5)+1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    if len(divs) != 0:
        if sum(divs) % 13 == 10:
            print(i, sum(divs))