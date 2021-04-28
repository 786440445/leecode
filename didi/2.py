def func():
    (n, m) = list(map(int, input().split(' ')))
    dp = {}
    while m > 0:
        m -= 1
        (i, j) = list(map(int, input().split(' ')))
        lis = dp.get(1, [])
        if i-1 in lis:
            lis.remove(i-1)
            dp[1] = lis
        else:
            lis.append(i-1)
            dp[1] = lis

        if j-1 in lis:
            lis.remove(j-1)
            dp[1] = lis
        else:
            lis.append(j-1)
            dp[1] = lis
    
    if dp[1] != []:
        return 'No'
    return 'Yes'
    
num = int(input())
while num > 0:
    ret = func()
    print(ret)
    num -= 1
