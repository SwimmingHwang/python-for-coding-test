'''
O(log N) 이 보장되지 못하는 답안임.
모범답안은 O(logN)보장
'''
n, m = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = n - 1

res = 0
while start <= end:
    if start == end:
        break
    mid = (start + end) // 2
    if li[mid] == m:
        r_mid = mid
        while li[mid] == m:
            mid -= 1
            res += 1
        mid = r_mid
        while li[mid] == m:
            mid += 1
            res += 1
        break
    elif li[mid] < m:
        start = mid + 1
    else:
        end = mid - 1

if res <= 0:
    print(-1)
else:
    print(res - 1)
'''
input
7 2
1 1 2 2 2 2 3 

4

7 4
1 1 2 2 2 2 3

-1 
'''

'''
모범답안 
1 - 이진 탐색 함수를 2개 작성하여 해결
- x가 처음 등장하는 인덱스와 마지막으로 등장하는 인덱스를 각각 계산한 뒤에, 인덱스 차이 계산
'''


def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1)
    if a is None:
        return 0
    b = last(array, x, 0, n - 1)
    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)


count = count_by_value(li, m)
print('method 1:', count)

'''
모범답안 
2 - bisect 라이브러리를 활용
'''
from bisect import bisect_left, bisect_right

a = bisect_left(li, m)
b = bisect_right(li, m)
print('method 2:', b - a)
