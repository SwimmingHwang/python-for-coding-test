'''
https://www.acmicpc.net/problem/11060
dp

10
1 2 0 1 3 2 1 5 4 2
1번 째 수 A1 A1이하 만큼 오른족으로 떨어진 칸으로 한번에 점프할 수 있다
3이면 1, 2, 3 으로 점프 가능
최소 몇번 점프 ?
  끝으로 갈 수 없는 경우에는 -1을 출력


*dp를 이용할 수 있는 문제 상황
- 큰 문제를 작은 문제로 나눌 수 있다.
- 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다


1 2 0 1 3 2 1 5 4 2

1에서 시작한다
A[1] = a, A[2] = b
  1
  2
  ...
  a
    A 1+1
    A 1+2
    A 1+a

- 거꾸로 가야할 듯
- 2 로 오는 경우가 얼마나 있을 까

1 2 0 1 3 2 1 5 4 2
              - -
5 -> 2 (5까지 올 수 있는 최소 점프 수)
  1 -> 5 (1까지 올 수 있는 최소 점프 수)
    2 -> 1
    3 -> 1

  2 -> 5
  3 -> 5
4 -> 2

- 큰 문제를 작은 문제로 나눌 수 있는가?
  - 본인 지점까지의 최소 점프수를 구하면 마지막 지점까지의 최소 점프 수를 구할 수 있으므로
   작은 문제로 나눠진다고 판단함 => dp
 - 본인 까지의 최소 점프수는 어떻게 구하는지?
  - 시작 지점부터 갈 수 있는 범위까지 dp 테이블을 업데이트 하면 dp 테이블이 초기화 된다

- 풀이법 : 자기(a)가 갈 수 있는 지점 모두 (예를 들어 3이면 본인자리(a)로 부터 +1, +2, +3 지점에다가 (a+1, a+2, a+3 지점에)
자기까지의 최소 점프수 값 (dp[a]) +1 과 이미 a+1, a+2, a+3 지점의 값 중 더 작은 값으로 dp 테이블 초기화 해 준다.

- 다른 풀이 :
  d[j] = d[i] + 1
'''

n = int(input())
li = list(map(int, input().split()))
dp = [int(1e9)] * (n+1)

dp[0] = 0

for i in range(n):
  for j in range(1, li[i]+1):
    if i+j > n:
      continue
    dp[i+j] = min(dp[i] +1, dp[i+j])

print(dp[n-1] if dp[n-1] != int(1e9) else -1)