'''
주의할 점 :
1. graph에는 (vertex, cost)
   우선순위 큐에는 (cost, vertex)
2. distance[start]에 0 초기화 잊지말기
'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))
    '''
    모범답안
    graph[x].append((y,z))
    '''


# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 잊지말기

    while q:
        now = heapq.heappop(q)  # distance, vertex
        if distance[now[1]] < now[0]:
            continue
        for v in graph[now[1]]:
            if distance[now[1]] + v[0] < distance[v[1]]:
                distance[v[1]] = distance[now[1]] + v[0]
                heapq.heappush(q, (distance[v[1]], v[1]))

    '''
    모범 답안
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]  # graph[(vertex,cost)]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]) 
    '''
dijkstra(c)
ans1 = 0
ans2 = 0
for i in distance[1:]:
    if i == INF:
        distance[i] = 0
    else:
        ans1 += 1
ans2 = max(distance[1:])

print(ans1 - 1, ans2)
'''
input
3 2 1 
1 2 4 
1 3 2

output
2 4
'''
