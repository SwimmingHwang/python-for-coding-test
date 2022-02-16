# 분할정복으로 풀어버
# n = int(input())
# r = n%2
# k = 1
#
# while n > 5:
#   n = n // 2
#   k *= 2
#   print(n, k)
#
# res = 0
# if n == 5:
#   res = k*2
# elif n == 4:
#   res = k*4
# elif n == 3:
#   res = k*2
# elif n == 2:
#   res = k*2
# else:
#   res = k
# if r == 0: #짝수면
#   print(res)
# else:
#   print((res + 2)%k)

from collections import deque
n = int(input())
q = deque([ i+1 for i in range(n)])
while len(q) >1:
  q.popleft()
  q.append(q.popleft())
print(q[0])