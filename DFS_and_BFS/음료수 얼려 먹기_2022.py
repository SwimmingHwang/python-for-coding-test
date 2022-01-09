'''
4 5
00110
00011
11111
00000
'''

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0


def dfs(graph, i, j, visited):
  visited[i][j] = True

  # 상 하 좌 우
  step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for s in step:
    dx = i + s[0]
    dy = j + s[1]

    if not (0 <= dx < n and 0 <= dy < m):
      continue
    if not visited[dx][dy] and graph[dx][dy] == 0:
      dfs(graph, dx, dy, visited)


for i in range(n):
  for j in range(m):
    if arr[i][j] == 0 and not visited[i][j]:
      cnt += 1
      dfs(arr, i, j, visited)

print(cnt)
