def func(strs):
    old_type = None
    count = 0
    for index, c in enumerate(strs):
        if index == 0:
            old_type = get_type(c)
        else:
            if get_type(c) != old_type:
                count += 1
    print(count)

def get_type(c):
    return type(c)


func(['a', 2, 3, 'b', 'c'])