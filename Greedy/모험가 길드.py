n = int(input())
li = list(map(int, input().split()))

cnt = 0
li.sort()

# i = 0
# while i < n and i + li[i] - 1 < n:
#     if li[i] == li[i + li[i] - 1]:
#         cnt += 1
#         i = i + li[i]
#     else:
#         break

result = 0
print(li)
for i in li:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)

'''
input
5
2 3 1 2 2
'''
