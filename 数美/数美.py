def func():
    filename = 'input.txt'
    arr = list(range(999))
    dict = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = int(line.strip())
            for i in arr:
                left = i * 100
                right = i * 100 + 99
                if left <= line <= right:
                    dict[i] = dict.get(i, 0) + 1
                    break

    for i, count in dict.items():
        left = i * 100
        right = i * 100 + 99
        print(str(left) + '-' + str(right) + ' ' + str(count))

# func()


def func1():
    dict = {}
    strs = ['a', 'b', 'a', 'c', 'a', 'b', 'b', 'c']
    for item in strs:
        dict[item] = dict.get(item, 0) + 1
        if dict[item] == 3:
            del dict[item]
    print(list(dict.keys())[0])


func1()
