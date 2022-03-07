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

  # 별표시가 가운데에 있는 경우 위치 찾아서 앞 뒤 비교
  if 0 < i < len(pattern) - 1 and str[-(len(pattern) - i - 1):] == pattern[i + 1:]:
    str = str[:-(len(pattern) - i - 1)] # 아래 반례와 같이 중복으로 꼭 들어가야 하지만 검사할 때 앞뒤를 검사하면 통과가 되기 때문에 한번 검사하면 없애준다
    if str[:i] == pattern[:i]:
      print("DA")
    else:
      print("NE")
  elif i == 0 and str[-(len(pattern) - i - 1):] == pattern[i + 1:]: # 별표시가 제일 앞에 있는 경우 뒤에 동일한지 검사
    print("DA")
  elif i == len(pattern) - 1 and str[:i] == pattern[:i]: # 별표시가 제일 뒤에 있는 경우 앞에까지 동일한지 검사
    print("DA")
  else:
    print("NE")

'''
반례
abcd*cdef
abcdef
'''
