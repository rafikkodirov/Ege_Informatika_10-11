with open('../files/24/24-s1.txt') as f:
    minN = 1000000000
    #print(f.read().count('V'))
    slovar = {}
    answer = []
    for line in f:
        countN = line.count('A')
        if countN < minN:
            minN, s = countN, line
    for x in s:
        if x in slovar:
            slovar[x] += 1
        else:
            slovar[x] = 1
    for key, value in slovar.items():
        if max(slovar.values()) == value:
            answer.append(key)
    print(max(answer))