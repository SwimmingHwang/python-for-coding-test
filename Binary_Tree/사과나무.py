'''
https://www.acmicpc.net/problem/2233
- 이진트리
- parent 를 구해야겠다
- stack 을 이용해서 parent를 구할 수 있겠다
- 문제에 맞게 풀이

'''

n = int(input())
bin_arr = list(map(int, list(input()))) # array 형태로 저장하려면 Map 함수 적용 후 list로 변환필요
x, y = map(int, input().split())

# n = 5
# bin_arr = list(
#   map(int, list('0001011011')))  # array 형태로 저장하려면 Map 함수 적용 후 list로 변환필요
# x, y = 4, 5

parent = [0] * (n + 1)
v_arr = []

stack = [0]
v = 1

for b in bin_arr:
  if b == 0:
    parent[v] = stack[-1]
    stack.append(v)
    v_arr.append(v)
    v += 1
  else:
    v_arr.append(stack.pop())

cut_x = v_arr[x - 1]
cut_y = v_arr[y - 1]

parent_x = []
parent_y = []

p = cut_x
while p != 0:
  parent_x.append(p)
  p = parent[p]

p = cut_y
while p != 0:
  parent_y.append(p)
  p = parent[p]

cut = max(set(parent_x) & set(parent_y))

print(*[i + 1 for i, x in enumerate(v_arr) if x == cut])
