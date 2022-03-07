'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
- 시간초과 : input readline 으로 변경 하니까 성공
'''

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i <= 0 and j <= 0:
      continue
    if i <= 0:
      arr[i][j] += arr[i][j-1]
    elif j <= 0:
      arr[i][j] += arr[i-1][j]
    else:
      arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]


for _ in range(m): # 10만
  x1, y1, x2, y2 = map(int, input().split())
  x1 -= 1  # 2
  y1 -= 1  # 2
  x2 -= 1  # 4
  y2 -= 1  # 4
  if x1 == 0 and y1 == 0:
    print(arr[x2][y2])
  elif x1 == 0:
    print(arr[x2][y2] - 0 - arr[x2][y1-1])
  elif y1 == 0:
    print(arr[x2][y2] - arr[x1-1][y2] - 0)
  else:
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])


# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# a = []
#
# max_x = 0
# max_y = 0
# for _ in range(m):  # 10만
#   li = list(map(int, input().split()))
#   a.append(li)
#   if max_x < li[2]:
#     max_x = li[2]
#   if max_y < li[3]:
#     max_y = li[3]
#
# for i in range(max_x):
#   for j in range(max_y):
#     if i <= 0 and j <= 0:
#       continue
#     if i <= 0:
#       arr[i][j] += arr[i][j - 1]
#     elif j <= 0:
#       arr[i][j] += arr[i - 1][j]
#     else:
#       arr[i][j] += arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1]
#
# for pos in a:
#   x1 = pos[0] - 1  # 2
#   y1 = pos[1] - 1  # 2
#   x2 = pos[2] - 1  # 4
#   y2 = pos[3] - 1  # 4
#   if x1 == 0 and y1 == 0:
#     print(arr[x2][y2])
#   elif x1 == 0:
#     print(arr[x2][y2] - 0 - arr[x2][y1 - 1])
#   elif y1 == 0:
#     print(arr[x2][y2] - arr[x1 - 1][y2] - 0)
#   else:
#     print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])

