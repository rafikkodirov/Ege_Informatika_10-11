'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [244143; 1367821], числа, имеющие
ровно 5 различных делителей. В ответе для каждого найденного числа запишите два его наибольших делителя,
не равных самому числу, в порядке возрастания.
'''
for i in range(244143, 1367822):
    divs = set()
    for d in range(1, round(i**0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
            if len(divs) > 5:
                break
    if len(divs) == 5:
        print(sorted(list(divs))[-3:-1])