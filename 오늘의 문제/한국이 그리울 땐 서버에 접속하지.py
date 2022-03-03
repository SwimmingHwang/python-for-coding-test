'''
https://www.acmicpc.net/problem/9996
'''

n = int(input())
pattern = input()

for _ in range(n):
  str = input()

  i = pattern.index('*')

  if len(pattern) == 1:
    print("DA")
    continue

  if 0 < i < len(pattern) - 1 and str[-(len(pattern) - i - 1):] == pattern[i + 1:]:
    str = str[:-(len(pattern) - i - 1)]
    if str[:i] == pattern[:i]:
      print("DA")
    else:
      print("NE")
  elif i == 0 and str[-(len(pattern) - i - 1):] == pattern[i + 1:]:
    print("DA")
  elif i == len(pattern) - 1 and str[:i] == pattern[:i]:
    print("DA")
  else:
    print("NE")

'''
반례
abcd*cdef
abcdef
'''
