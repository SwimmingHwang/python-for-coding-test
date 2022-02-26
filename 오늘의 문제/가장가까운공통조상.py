'''
https://www.acmicpc.net/problem/3584
'''

import sys
input = sys.stdin.readline
t = int(input())

a, b = 0, 0
for i in range(t):
  n = int(input())
  graph = [[] for _ in range(n + 1)]
  for j in range(1, n):
    v1, v2 = map(int, input().split())
    graph[v1].append((v2, -1))
    graph[v2].append((v1, 1))
  a, b = map(int, input().split())

  a_list = graph[a][:]
  b_list = graph[b][:]

  a_answer = [a]
  b_answer = [b]

  while a_list:
    g = a_list.pop()
    if g[1] < 0:
      continue
    a_list = graph[g[0]][:]
    a_answer.append(g[0])

  while b_list:
    g = b_list.pop()
    if g[1] < 0:
      continue
    b_list = graph[g[0]][:]
    b_answer.append(g[0])

  a_answer = a_answer[::-1]
  b_answer = b_answer[::-1]

  for x in range(min(len(a_answer), len(b_answer))):
    if a_answer[x] != b_answer[x]:
      print(a_answer[x - 1])
      break
  else:
    print(a_answer[x])

# TODO : 1. parent array 초기화 하고 그 두개의 parent 거슬러 올라가면서 비교
# 2. visited array둬서 동일한거 visited면 true