'''
nil nil nil G F nil nil C nil nil E nil D B A end
를 그래프로 만들기
- 여기서 그래프는 부모 노드 parent array 채우기
- 입력받은 string array 앞에서 부터 순회하면서
- nil 일때는 다 stack에 넣고 아니면
  nil 이 아니면 stack 두 번 pop 에서 그 두 개 parent로 세팅
- 부모가 다르면 동일하지 않은 트리임
  -> parent 노드 찾는 함수 및 코드 구현 필요

'''

import sys

input = sys.stdin.readline

t = int(input())


def find_parent_node(graph, parent):
  stack = []

  for g in graph:  # G
    if g == 'nil':
      stack.append(chr(ord('A')-1))  # 말단노드 이면 stack에 append 만
    else:
      if len(stack) >= 2:  # G
        left = stack.pop()  # nil
        right = stack.pop()  # nil
        parent[ord(left)-ord('@')] = g
        parent[ord(right)-ord('@')] = g
      stack.append(g)  # nil G

  while stack:
    p = stack.pop()
    if p == 'end':
      continue
    else:
      parent[0] = p

  return parent


for a in range(t):
  parent1 = [0] * 27  # nil ~ A ~ Z
  parent2 = [0] * 27

  g1 = input().split()
  g2 = input().split()

  parent1 = find_parent_node(g1, parent1)
  parent2 = find_parent_node(g2, parent2)

  print('true' if parent1 == parent2 else 'false')

# TODO : 수진이 코드 보기, parent 거슬러 올라가는거 stack, queue 쓰는 것 만 생각하기!
# TODO : parent 에 A의 자식이 B,F 면 B랑 F 에 부모인 A가 들어가 있다
