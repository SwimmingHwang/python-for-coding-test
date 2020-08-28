'''
- M의 최대 크기가 10000이므로 불가능한 수로 10001로 설정해야 함.
- 0원의 경우 화폐를 하나도 사용하지 않았을 때 만들 수 있으므로 값으로 0 설정해야 함.

- 런타임에러 : 배열 array 조건문 무조건 넣어주기!

[모범답안]
점화식 :
ai = min(a_i, a_i-k +1)
모든 화폐 단위에 대해서 작은 DP table을 업데이트 해준다.
첫번째 회폐 단위 - dp update
두번째 화폐 단위 - dp update
'''

import sys

n, m = map(int, input().split())
d = [10001] * (m + 1)

d[0] = 0

coin = []
for ci in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))
coin.sort()

# print(coin)
for i in range(coin[0], m + 1):
    # print('i = ',i)
    if i in coin:  # 화폐 단위인 경우 1 넣어주기
        d[i] = 1
    else:
        min_val = 10001
        for j in range(0, n):  # 화폐 단위만큼 빼준 위치들의 최소 갯수 구하기
            if i - coin[j] > 0:
                if d[i - coin[j]] > 0:
                    if d[i - coin[j]] < min_val:
                        min_val = d[i - coin[j]]
                        d[i] = min_val + 1

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

'''
input
2 15
2
3

3 4
3
5
7

3 15
1
5
12

'''

'''
모범 답안
'''
array = coin
# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)