
def func(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    dp = [[0]*l1 for _ in range(l2)]
    start_index = 0
    end_index = 0
    max_l = 0
    for i in range(l2):
        for j in range(l1):
            if str2[i] != str1[j]:
                dp[i][j] = 0
            else:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > max_l:
                max_l = dp[i][j]
                end_index = i + 1
                start_index = i - max_l + 1
    return str2[start_index:end_index]

str1 = '1AB21255CD'
str2 = '1321255as'
a = func(str1, str2)
print(a)