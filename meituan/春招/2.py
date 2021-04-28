
[n,m] = map(int, input().split(' '))

A = map(int, input().split(' '))
B = map(int, input().split(' '))

da = {}
for c in A:
    da[c] = da.get(c, 0) + 1
for c in B:
    db[c] = db.get(c, 0) + 1

da = sorted(da.items(), key=lambda x: x[1])
db = sorted(db.items(), key=lambda x: x[1])
n = da[0][0]

for x in range(n):
    if da
    
    pass
