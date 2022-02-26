s = input()

for i in range(len(s)//2): # level 0 1 2 3 4  => 0, 1
  if s[i] == s[len(s)-1-i]:
    continue
  else:
    print(0)
    break
else:
  print(1)



