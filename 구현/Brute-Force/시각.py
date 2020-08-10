"""
brute force
내 답안
- 모범답안 처럼 if문을 한 문장으로 줄일 수 있음
"""
n = int(input())

res = 0
for i in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(i):
                res += 1
                continue
            if '3' in str(m):
                res += 1
                continue
            if '3' in str(s):
                res += 1
                continue
print(res)
"""
모범 답안
"""

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)