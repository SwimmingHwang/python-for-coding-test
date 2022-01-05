'''
https://www.acmicpc.net/problem/5014

10 1 10 2 1

'''

f, s, g, u, d = (map(int, input().split()))

op = 1
cur = s
res = 0

if s == g:
  print(0)

while cur != g:
  print(cur, g)
  if cur < g:
    print('+++')
    op = 1
    res += abs(g - cur) // u
    cur += op * int(abs(g - cur) / u) * u
  else:
    print('---')

    if d == 0:
        print("use the stairs 1 ")
        break

    op = -1
    res += int(abs(g - cur) / d)
    cur += op * int(abs(g - cur) / d) * d

  print('res ' + str(res))

  if abs(cur-g) % abs(u-d) != 0:
    print(abs(cur-g) ,abs(u+d))
    print("use the stairs 2 ")
    break

print(f, s, g, u, d)
