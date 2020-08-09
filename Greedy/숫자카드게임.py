"""
max(iterable data)  함수 사용하면 더 간결함
"""
n, m = map(int, input().split())
res = -1
for _ in range(n):
    m = min(list(map(int, input().split())))
    if res < m:
        res = m

print(res)
