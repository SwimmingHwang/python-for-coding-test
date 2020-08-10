"""
내 답안 pm 6:00까지
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

c_x += 1
c_y += 1
arr[c_x][c_y] = 1
cnt = 1

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
        arr[c_x] = 2
        arr[c_y] = 2
    print(arr)

    # 3단계 다 가본 칸이거나 바다인 경우
    if arr[c_x - 1] != 0 and arr[c_x + 1] != 0 and arr[c_y + 1] != 0 and arr[c_y - 1] != 0:
        # 뒤가 바다면 멈춤
        dx, dy = steps[(c_d + 2) % 4]
        if arr[c_x + dx][c_y + dy] == 1:
            break
        else:
            c_x += dx
            c_y += dy
    print(arr)
print(cnt)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''