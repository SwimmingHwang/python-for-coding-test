"""
틀린 답안
원인 분석
1. 넓은 관점으로 고민하지 못하고 나누어 떨어지지 않는 경우에 해당하는 답안을 고려함.
2. 접근을 잘 못 했었음.
"""

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
print(a)
# sorted list
a.sort(reverse=True)
print(a)
m1 = a[0]
m2 = a[1]

res = (m // k * k * m1) + (m % k * m2)
print(res)

"""
답안
"""
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
print(a)
# sorted list
a.sort(reverse=True)
print(a)
m1 = a[0]
m2 = a[1]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * m1
count += m % (k + 1)

res = 0
res += count * m1
res += (m - count) * m2
print(res)
