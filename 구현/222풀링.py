'''
4
-6 -8 7 -4
-5 -5 14 11
11 11 -1 -1
4 9 -2 -4

11
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# for cnt in range(n**(1/2)):
while n != 1:
  n = n//2
  for i in range(n):
    for j in range(n):
      di = i * 2
      dj = j * 2
      li = [arr[di][dj], arr[di+1][dj], arr[di][dj+1], arr[di+1][dj+1]]
      li.sort(reverse=True)
      arr[i][j] = li[1]

print(arr[0][0])




