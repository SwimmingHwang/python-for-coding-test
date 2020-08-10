"""
simulation
내 답안(pm4:56)
[기억할 점]
- 시뮬레이션 문제에서 자주 사용되므로, 상하좌우 문제의 dx, dy처럼 이동할 방향을 정의해서 사용하기
- 이동하고자 하는 위치를 확인 -> 이동가능한 조건 한 번에 검사 후 카운트 증가
- ord() 함수 기억하기
    : Return the Unicode code point for a one-character string.
"""

h = input()  # a1
x = int(ord(h[0]) - 96)
y = int(h[1])

cnt = 0

if x - 2 >= 1:
    if y - 1 >= 1:
        cnt += 1
    if y + 1 <= 8:
        cnt += 1

if x + 2 <= 8:
    if y - 1 >= 1:
        cnt += 1
    if y + 1 <= 8:
        cnt += 1

if y - 2 >= 1:
    if x - 1 >= 1:
        cnt += 1
    if x + 1 <= 8:
        cnt += 1
if y + 2 <= 8:
    if x - 1 >= 1:
        cnt += 1
    if x + 1 <= 8:
        cnt += 1
print(cnt)

"""
모범 답안
"""

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]) - ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

# 8가지방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 바로 조건문을 쓰는게 아니라 이동하고자 하는 위치를 먼저 확인 -> 가능하면 카운트 증가
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    # 조건도 한 번에 검사
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)


