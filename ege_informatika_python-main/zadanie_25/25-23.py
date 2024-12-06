'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [338472; 338494], числа,
имеющие ровно 4 различных делителя. В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания
'''
for i in range(338472, 338495):
    divs = set()
    for d in range(1, round(i**0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(sorted(list(divs))[-2:])