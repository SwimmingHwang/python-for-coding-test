'''
위상정렬
- 그래프
- 진입차수 리스트
- 큐
'''

from collections import deque

n = int(input())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
result = [0] *(n+1)


for i in range(1, n + 1):
    edges = list(map(int, input().split()))
    cost = edges[0]
    for edge in edges[1:]:
        if edge == -1:
            break
        graph[i].append((cost, edge))
        indegree[i] += 1

print(indegree)
print(graph)



def topology_sort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            cost = graph[i][0]
            q.append((i, cost))
    print(q)
    while q:
        now, cost_now = q.popleft()
        print(now, cost_now)
        result[now] += cost_now

        li = []
        for i in graph[now]:
            cost_v, v = i
            indegree[v] -= 1
            if indegree[v] == 0 :
                li.append((cost_v, v))

        li.sort()
        for l in li:
            cost_v, v = l
            if indegree[v] == 0:
                q.append((v, cost_now+cost_v))



topology_sort()
print(result)

'''
input
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''