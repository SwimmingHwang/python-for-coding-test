# 그래프 - 플로이드 워샬 알고리즘으로 풀기

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
path = [[[]] * (n + 1)  for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  # A와 B가 서로에게 가는 비용은 cost 이라고 설정
  a, b, cost = map(int, input().split())
  if graph[a][b] > cost:
    graph[a][b] = cost
    path[a][b] = [a, b]

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      if graph[a][b] > graph[a][k] + graph[k][b]:
        graph[a][b] = graph[a][k] + graph[k][b]
        path[a][b] = path[a][k][:-1] + path[k][b]

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print(0, end=" ")
    else:
      print(graph[a][b], end=" ")
  print()

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print(0)
    else: # 도시의 개수, 경로
      li = path[a][b]
      print(len(li), end=' ')
      for l in li:
        print(l, end=' ')

    print()
