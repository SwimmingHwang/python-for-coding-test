from collections import deque


def bfs(graph, start, visited, k):
    res = []
    q = deque()
    visited[start] = 0
    q.append(start)

    cnt = 1

    while q:
        now = q.popleft()
        cnt = visited[now]
        for i in graph[now]:
            if visited[i] == INF:
                q.append(i)
                visited[i] = cnt+1
                if visited[i] == k:
                    res.append(i)
    return res

n, m, k, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]  # 인접리스트 그래프 초기화

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [INF] * (n + 1)
res = bfs(graph, x, visited, k)

res.sort()
for i in res:
    print(i)
if not res:
    print(-1)
'''
input
4 4 2 1
1 2
1 3 
2 3
2 4 
'''