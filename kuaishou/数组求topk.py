
from heapq import *


def func(arr, k):
    heap = []
    for s in arr:
        for c in s:
            heappush(heap, -c)

    ret = []
    while k > 0:
        c = heappop(heap)
        ret.append(-c)
        k -= 1
    return ret


res = func([[14, 26, 34], [22, 26, 33], [11, 47, 87]], 5)
print(res)

