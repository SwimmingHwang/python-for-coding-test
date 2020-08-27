'''
- dp table 100으로 해야 함
'''

n = int(input())
k = list(map(int, input().split()))

# DP table
d = [0]*1001

d[1] = k[1]

for i in range(2, n+1):
    d[i] = max(d[i-1],  k[i-1] + d[i-2])
print(d[n])

'''
input
4
1 3 1 5
'''