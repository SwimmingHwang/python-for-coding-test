'''
       col col
       |
       v
       0   1   2   3
row -> 1
2
..
n
'''

'''
dfs( row=0)        cnt = 0
  col=0 [0, , , ]
  dfs( row=1) break  cnt = 0 


풀이 참고 : https://rebas.kr/761
'''

n = int(input())


def dfs(queen, n, row):
  cnt = 0

  if n == row:
    return 1

  for col in range(n):
    queen[row] = col  # queen [0, 0,

    for x in range(row):  # x는 0, row 는 1
      if queen[x] == queen[row]:  # 같다는 것은 같은 컬럼에 있다는 거니까 세로로 겹치는 경우
        break
      if abs(queen[x] - queen[row]) == (row - x):  # 대각선으로 겹치는 경우
        break

    else:  # 가로는 애초에 안겹치게 만들었고,
      # 세로랑 대각선으로 겹치지 않으면 dfs로 이어서 진행 (break로 탈출하지 않은 경우 else 로)
      cnt += dfs(queen, n, row + 1)

  return cnt

queen = [0] * n
# 각 row에는 하나의 값만 들어가기 때문에 일차원 리스트로 만듦
# ex [1, 3, 0, 2] 라면 0 row에 1에 배치, 1 row에 3 배치.. 라는 뜻
print(dfs(queen, n, 0))
