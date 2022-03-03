import heapq

INF = int(1e9)


def dijkstra(start, distance, graph):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      # print(i)
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  return distance


def solution(n, edge):
  answer = 0

  graph = [[] for _ in range(n+1)]
  distance = [INF] * (n + 1)

  for e1, e2 in edge:
    graph[e1].append((e2, 1))
    graph[e2].append((e1, 1))

  distance = dijkstra(1, distance, graph)
  max_dist = max(distance[1:])
  answer = distance.count(max_dist)
  return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
'''
다른 풀이
cost랑 상관없이 그냥 방문안했으면 queue에 넣고 distance에 본인 distance에 인접 distance value +1 해주기 

def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)] # 방문 array
     
    queue = [0]
    is_visit[0] = True
    
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer
'''