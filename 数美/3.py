import math

def func():
    with open('input.txt', 'r', encoding='utf-8') as f:
        dict = {}
        for line in f.readlines():
            line = line.strip()
            if line != '':
                line = line.split(' ')
                id = line[0]
                macid = line[1]
                info = dict.get(id, [{}, 0])
                dic = info[0]
                sum = info[1]
                sum += 1
                dic[macid] = dic.get(macid, 0) + 1
                dict[id] = [dic, sum]

    for id, info in dict.items():
        dic = info[0]
        sum = info[1]
        entropy = 0
        for macid, mac_num in dic.items():
            p = mac_num / sum
            entropy -= p * math.log(p, 2)
        print(str(id) + ' , ' + str(entropy))

func()