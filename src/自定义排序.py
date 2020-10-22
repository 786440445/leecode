import functools


# 从大到小 # 当cmp返回是正数时 交换两元素
def cmp(a, b):
    if b[0] < a[0]:
        return -1
    if b[0] > a[0]:
        return 1
    if b[1] < a[1]:
        return -1
    if b[1] > a[1]:
        return 1
    return 0

# 从小到大
def cmp1(a, b):
    if b[0] < a[0]:
        return 1
    if b[0] > a[0]:
        return -1
    if b[1] < a[1]:
        return -1
    if b[1] > a[1]:
        return 1
    return 0


a = [[1, 1], [1,2], [2, 5], [2, 3], [2, 4]]
print(sorted(a, key=functools.cmp_to_key(cmp1)))
