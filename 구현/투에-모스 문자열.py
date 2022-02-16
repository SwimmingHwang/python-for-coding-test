# k = int(input())
# x = '01'
# n = k
# while k // 2 > 0:
#   k = k//2
#   new_x = ''.join([ str(ord('1')- ord(i)) for i in x])
#   x += new_x
#
# print(n)
# print(x[n-1])
#
# # while 문 마다 매번 새로운 string 만든다

k = int(input())
def recursive(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n%2:
    return 1-recursive(n//2)
  else:
    return recursive(n//2)
print(recursive(k-1))