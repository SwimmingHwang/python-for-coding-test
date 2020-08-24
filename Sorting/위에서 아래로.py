"""
list.sort()와 sorted(list) 차이
1. list.sort()
- 원본 리스트를 정렬하되 반환 값은 None
- 원본 리스트의순서를 변경함 (원본 리스트에 영향 있음)
2. sorted(list)
- 정렬된 새로운 리스트를 반환함 (원본 리스트에 영향 없음)
- 모든 iterable에 동작함 (list, tuple, dict, 문자열)
"""
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li.sort(reverse=True)
# li = sorted(li, reverse=True) 와 동일

for i in li:
    print(i,end=' ')

'''
input
3
15
27
12
'''
'''
output
27 15 12 
'''
