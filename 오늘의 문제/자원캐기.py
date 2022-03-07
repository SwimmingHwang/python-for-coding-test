n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# n, m = 5, 4
# arr = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0]]
arr2 = [[0] * m for _ in range(n)]


for i in range(n):
  for j in range(m):
    if j == 0 or i == 0:
      if j == 0 and i == 0:
        arr2[i][j] = arr[i][j]
      elif j == 0:
        arr2[i][j] = arr2[i-1][j] + arr[i][j]
      else:
        arr2[i][j] = arr2[i][j-1] + arr[i][j]
    else:
      arr2[i][j] = max(arr2[i-1][j], arr2[i][j-1]) + arr[i][j]

# print(arr2)

print(arr2[n-1][m-1])


