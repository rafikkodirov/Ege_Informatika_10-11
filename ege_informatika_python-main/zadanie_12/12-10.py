'''
Дана программа для исполнителя Редактор:
ПОКА нашлось (555) ИЛИ нашлось (888)
  заменить (555, 8)
  заменить (888, 55)
КОНЕЦ ПОКА
Известно, что начальная строка состоит более чем из 200 цифр 5 и не содержит других символов.
В ходе работы алгоритма получилась строка, содержащая больше цифр 8, чем цифр 5. Укажите минимальную возможную длину входной строки.
'''
for i in range(201, 1000):
    s = i * '5'
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    if s.count('8') > s.count('5'):
        print(i)
        break