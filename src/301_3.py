# def func():
#     str_x = input().split(',')
#     str_x = sorted(str_x, key=sort_func, reverse=False)
#     ret = ''.join(str_x)
#     while ret[0] == '0':
#         ret = ret[1:]
#     print(ret)
#
#
# class sort_func(str):
#     def __lt__(x, y):
#         x_l = len(x)
#         y_l = len(y)
#         if x_l == y_l:
#             return x > y
#         else:
#             return x+y > y+x
#
# func()


def func111():
    n = int(input())
    count_dict = {}
    while(n):
        inp = [int(x) for x in input().split(' ')]
        from_avid, to_avid = inp[0], inp[1]
        count_dict[from_avid] = count_dict.get(from_avid, 0) + 1
        n -= 1
    sort_dict = sorted(count_dict.items(), key=sort_func111)

    print(sort_dict[0][0])


class sort_func111(list):
    def __lt__(x, y):
        if x[1] == y[1]:
            return x[0] > y[0]
        return x[1] > y[1]
func111()