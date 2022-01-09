'''
https://www.acmicpc.net/problem/4963
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

0
1
1
3
1
91 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

while True:
  m, n = map(int, input().split())
  if not 0 and not m:
    break
  arr = [list(map(int, input().split())) for _ in range(n)]
  visited = [[False] * m for _ in range(n)]
  cnt = 0

  def dfs(graph, i, j, visited):
    visited[i][j] = True

    # 상 하 좌 우
    step = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for s in step:
      dx = i + s[0]
      dy = j + s[1]

      if not (0 <= dx < n and 0 <= dy < m):
        continue
      if not visited[dx][dy] and graph[dx][dy] == 1:
        dfs(graph, dx, dy, visited)


  for i in range(n):
    for j in range(m):
      if arr[i][j] == 1 and not visited[i][j]:
        cnt += 1
        dfs(arr, i, j, visited)

  print(cnt)
