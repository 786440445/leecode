s = input()

length = len(s)
result = [[False for _ in range(length)] for _ in range(length)]
max_l = 0
for l in range(length):
    for i in range(length):
        j = i + l
        if j >= length:
            break
        if l == 0:
            result[i][j] = True
        elif (l == 1 and s[i] == s[j]) or (l == 1 and (s[i] == '*' or s[j] == '*')):
            result[i][j] = True
        else:
            result[i][j] = result[i+1][j-1] and (s[i] == s[j] or s[i] == '*' or s[j] == '*')
        if result[i][j] and l + 1 > max_l:
            max_l = l + 1
print(max_l)