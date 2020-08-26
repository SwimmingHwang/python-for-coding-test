"""
https://www.acmicpc.net/problem/2805 나무자르기 각색문제
- 모범답안에서는 굳이 make_sum함수를 만들지 않고 계산함.
- 다른 경우를 생각하지 못했음.
    :만약 m과 완벽히 일치하지 않은 경우엔 최대한 덜 잘랐을 때가 정답인 경우를 기록해줘야 함
- 굳이 input list를 정렬하지 않아도 됨.
"""

n, m = map(int, input().split())
li = list(map(int, input().split()))

# li.sort()  # 내림차순 정렬  - 필요없음


def make_sum(arr, sub_val):
    res = 0
    for i in arr:
        val = i - sub_val
        res += (val if val > 0 else 0)
    return res


start = 0
end = max(li)
# end = li[-1]

while start <= end:
    mid = (start + end) // 2
    mid_val = make_sum(li, mid)
    print(mid, mid_val)
    if mid_val == m:
        result = mid
        break
    elif mid_val < m:  # 더 잘라도 됨
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
'''
input 
4 6
19 15 10 17
'''
'''
output
15
'''
"""
모범 답안
"""
array = li

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
