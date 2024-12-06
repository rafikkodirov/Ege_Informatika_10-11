'''
В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
Определите и запишите в ответе сначала количество пар элементов последовательности, у которых разность элементов
кратна 45 и хотя бы один из элементов кратен 18, затем максимальную из разностей элементов таких пар. В данной задаче
под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
'''
with open('../files/17/17-r4.txt') as f:
    s = [int(x) for x in f]
    numbers = []
    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            if ((s[i] - s[j]) % 45 == 0) and (s[i] % 18 == 0 or s[j] % 18 == 0):
                numbers.append(s[i] - s[j])
    print(len(numbers), max(numbers))