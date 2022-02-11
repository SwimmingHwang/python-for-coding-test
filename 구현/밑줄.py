'''
9 50
A
quick
brown
fox
jumps
over
the
lazy
dog

4 19
hello
world
John
Said

5 27
Alpha
Beta
Gamma
Delta
Epsilon

3 8
a
b
C
 
'''
n, m = map(int, input().split())

li = [input() for _ in range(n)]
count = 0
for l in li:
  count += len(l)

if count < m:
  q = (m - count) // (n - 1)
  r = (m - count) % (n - 1)

  if r != 0:
    for i in range(n):
      if r == 0:
        break
      if i == 0:
        continue
      if 'a' <= li[i][0] <= 'z':
        li[i] = '_' + li[i]
        r -= 1

    for i in range(len(li) - 1, -1, -1):  # 역순 순회
      if r == 0:
        break
      if not 'a' <= li[i][0] <= 'z':
        li[i] = '_' + li[i]
        r -= 1

  print(("_" * q).join(li))
else:
  print("".join(li))
