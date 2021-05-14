# 快速排序函数
def quickSort(arr, low, high, time):
    if low < high:
        pi = quick_index(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def quick_index(arr, left, right):
    low = left
    high = right
    mid = arr[left]
    while low < high:
        while low < high and arr[high] <= mid:
            high -= 1
        if low < high:
            arr[low] = arr[high]

        while low < high and arr[low] > mid:
            low += 1
        if low < high:
            arr[high] = arr[low]
    arr[low] = mid
    return low

# 快排求topk
def min_num(arr, m):
    sum = 0
    start, end = 0, len(arr) - 1
    index = quick_index(arr, start, end)
    while index != m:
        if index < m:
            index = quick_index(arr, index + 1, end)
        else:
            index = quick_index(arr, start, index)
        if index % 2 == 1:
            sum += arr[index]
    return sum


if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split(' ')))
    time = int(N / 2)
    ret = min_num(array, time)
    sum = 0
    for index, item in enumerate(ret):
        if index % 2 == 1:
            sum += item
    print(sum)