'''
5 5
1 1 1  1번 기차에 1 번째 좌석에 사람을 태워라 이미
1 1 2  1번 기차에 1번째에  명
1 2 2  2번 기차에 2번째에
1 2 3  1번 기차에 2번째 좌석에 3명
3 1    1번 기차에


1: 승차
2 하차
3 모두 한칸씩 뒤로
4는 앞으로 이
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

train = [[0] * 20 for _ in range(n)]

for _ in range(m):

  s = list(map(int, input().split()))
  op = s[0]
  i, x = 0, 0

  if op == 1:
    i, x = s[1]-1, s[2]-1
    train[i][x] = 1
  elif op == 2:
    i, x = s[1]-1, s[2]-1
    train[i][x] = 0
  elif op == 3:
    i = s[1]-1
    train[i].insert(0, 0)
    train[i].pop()
  elif op == 4:
    i = s[1]-1
    train[i].append(0)
    train[i].pop(0)

# cnt = 0
# for t1_index, t1 in enumerate(train):
#   flag = False
#   for t2 in train[0: t1_index]:
#     if t1 != t2:
#       flag = True
#       continue
#     else:
#       flag = False
#       break
#   if flag:
#     cnt += 1

answer = []
for t in train:
  if t not in answer:
    answer.append(t)

print(len(answer))
