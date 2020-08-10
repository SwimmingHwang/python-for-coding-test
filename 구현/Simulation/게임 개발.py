"""
simulation
내 답안
- 문제를 이해하기 어려웠음.
- 디버깅도 오래걸림
- 흐름을 잘 구현하지 못함.
- 시간 초과
- 문제 지문을 단순화해서 구현할 수 있어야 함.  (너무 복잡하게 생각함)
---------
- 방향정의 :
dx = [-1,0,1,0]
dy = [0,1,0,-1]
이렇게 하는 것이 효과적임.
- 반복적인 숙달 필요
"""

n, m = map(int, input().split())
c_x, c_y, c_d = map(int, input().split())

arr = [[1] * (m + 2)]
for _ in range(n):
    li = [1]
    li.extend(list(map(int, input().split())))
    li.append(1)
    arr.append(li)
arr.append([1] * (m + 2))

# 테두리 만들어 줬기 때문에 좌표 1씩 더해주기
c_x += 1
c_y += 1
arr[c_x][c_y] = 2 # 방문하면 2로 표기
cnt = 1 # 시작점 방문해서 cnt +1 로 시작

# 방향 정의
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while True:
    # 1 단계 왼쪽 방향으로 회전
    dx, dy = steps[(c_d + 3) % 4]
    # 2단계 바로 왼쪽으로 이동 (안가봤다면)
    if arr[c_x + dx][c_y + dy] == 0:
        cnt += 1
        c_x += dx
        c_y += dy
        c_d = (c_d + 3) % 4
        arr[c_x][c_y] = 2

    # 3단계 다 가본 칸이거나 바다인 경우
    elif arr[c_x - 1][c_y] != 0 and arr[c_x + 1][c_y] != 0 and arr[c_x][c_y + 1] != 0 and arr[c_x][c_y - 1] != 0:
        # 뒤가 바다면 멈춤
        dx, dy = steps[(c_d + 2) % 4]
        if arr[c_x + dx][c_y + dy] == 1:
            break
        else:
            c_x += dx
            c_y += dy
    else:
        c_d = (c_d + 3) % 4
        continue

print(cnt)

'''
input : 
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
output : 3
'''

"""
모범 답안
"""
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)