"""
- 오름차순 내림차순 삽질함. 잘 보기
- 키로 정렬시 람다함수 사용하면 더 간단함.
"""
n = int(input())
li = []

for _ in range(n):
    l = input().split()
    l[1] = int(l[1])
    li.append((l[0], l[1]))

# 키값으로 정렬
def setting(data):
    return data[1]

li = sorted(li, key=setting)
# li = sorted(li, key=lambda student: student[1])

for i in li:
    print(i[0], end=' ')

'''
input
2
홍길동 95
이순신 77
'''
'''
output
이순신 홍길동
'''
