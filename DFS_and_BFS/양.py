'''
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###

'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

r, c = map(int, input().split())

map = [list(list(input())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

res_s, res_w = 0, 0
sheep, wolf = 0, 0


def dfs(graph, i, j, visited):
  global sheep, wolf

  visited[i][j] = True

  if graph[i][j] == 'o':
    sheep += 1
  elif graph[i][j] == 'v':
    wolf += 1

  step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for s in step:
    dx = i + s[0]
    dy = j + s[1]

    if not (0 <= dx < r and 0 <= dy < c):
      continue
    if not visited[dx][dy] and graph[dx][dy] != "#":
      dfs(graph, dx, dy, visited)


for i in range(r):
  for j in range(c):
    if not visited[i][j] and map[i][j] != "#":
      dfs(map, i, j, visited)
      if sheep > wolf:
        res_s += sheep
      else:
        res_w += wolf
      sheep = 0
      wolf = 0


print(res_s, res_w)