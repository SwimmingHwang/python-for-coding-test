n = int(input())

arr = [input() for _ in range(n)]

res = ''
for i in range(len(arr[0])):
  ch = arr[0][i]
  for j in range(1, n):
    if arr[j][i] == ch:
      continue
    else:
      res += '?'
      break
  else:
    res += ch

print(res)
