'''
В файле 17-282.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения
от 0 до 10 000. Определите количество пар элементов последовательности, в которых хотя бы у одного из чисел сумма цифр
равна сумме цифр минимального элемента последовательности, кратного 37. В ответе запишите количество найденных пар,
затем минимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
with open('../files/17/17-282.txt') as f:
    s = [int(x) for x in f]
    numbers = []
    min37 = min([t for t in s if t % 37 == 0])
    for i in range(len(s) - 1):
        if sum(map(int, str(s[i]))) == sum(map(int, str(min37))) or sum(map(int, str(s[i + 1]))) == sum(map(int, str(min37))):
            numbers.append(s[i] + s[i + 1])
print(len(numbers), min(numbers))