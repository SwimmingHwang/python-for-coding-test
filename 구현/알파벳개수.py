from collections import Counter

s = input()

count = Counter(s)

for i in range(ord('z') - ord('a')+1):
  print(count[chr(i+ord('a'))], end=' ')
