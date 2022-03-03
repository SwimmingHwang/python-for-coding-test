'''
https://www.acmicpc.net/problem/2194
'''

from collections import deque

# 입력
n, m, a, b, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for _ in range(k):
  row, col = map(int, input().split())
  arr[row - 1][col - 1] = -1

start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())


# BFS
step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cur_x, cur_y = start_x-1, start_y-1

q = deque([(cur_x, cur_y)])  # 괄호 해 줘야 tuple이 insert 됨
visited[cur_x][cur_y] = 0

while q:
  cur_x, cur_y = q.popleft()

  for dx, dy in step:
    x = cur_x + dx
    y = cur_y + dy

    flag = True

    if not (0 <= x < n and 0 <= y < m and 0 <= x+a-1 < n and 0 <= y+b-1 < m):
      continue

    for i in range(a):
      for j in range(b):
        if arr[x + i][y + j] == -1:
          flag = False

    if flag and visited[x][y] == 0:
      q.append((x, y))
      visited[x][y] = visited[cur_x][cur_y] + 1

res = visited[end_x-1][end_y-1]
print(-1 if res == 0 else res)