from collections import deque


def bfs(graph, start, visited):
  queue = deque([start])

  visited[start] = True

  while queue:
    # 큐에서 하나의 원소를 봅아 출력
    v = queue.popleft()
    print(v, end=' ')

    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


# 각 노드가 방문된 저보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
# 정의된 DFS 함수 호출
bfs(graph, 1, visited)
