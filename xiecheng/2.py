def func():
    array = list(map(int, input().split(',')))
    l = len(array)
    if l == 0:
        return 0
    dp = [0]*l
    
    for index in range(l):
        if index == 0:
            dp[index] = array[index]
        elif index == 1:
            dp[index] = max(array[index], dp[index-1])
        else:
            dp[index] = max(dp[index-2] + array[index], dp[index-1])
    return dp[l-1]
    
if __name__ == '__main__':
    ret = func()
    print(ret)