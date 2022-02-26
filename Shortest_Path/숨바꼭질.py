import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)


for _ in range(m): # 인접행렬 방식
  a_i, b_i = map(int, input().split())
  graph[a_i].append((b_i, 1))
  graph[b_i].append((a_i, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))  # cost, vertex
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for v in graph[now]:
      cost = dist + 1
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        heapq.heappush(q, (cost, v[0]))


dijkstra(1)

# 첫 번째는 숨어야 하는 헛간 번호를(만약 거리가 같은 헛간이 여러개면 가장 작은 헛간 번호를 출력한다),
# 두 번째는 그 헛간까지의 거리를,
# 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력해야한다.
distance = distance[1:]
maxDistance = max(distance)

print(distance.index(maxDistance)+1, maxDistance, distance.count(maxDistance))

# 연결리스트형, 인접행렬형 뭐가 나았을까 이 문제에서?
# 전보에서는 연결리스트 형으로 구현해서 각색이 필요한 상태임
# 방향이 없어서..
# 전보 문제 다시보기
# 연결리스트형으로 해야 된다
# 다익스트라 알고리즘이 최단 경로 알고리즘이며, 1 넣으면 1에서의 최단 경로를  할 수 있는데..
# 이에 대한 이해가 부족함을 깨닳았다
# 양방향으로 넣어줘야 했다


# TODO : BFS로 depth 저장해 가면서 풀 수 있음