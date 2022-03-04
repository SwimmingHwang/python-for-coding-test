'''
https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3#
'''

from itertools import combinations
from collections import Counter


def solution(orders, course):
  answer = []
  arr = [[] for _ in range(len(course))]

  for order in orders:
    for i, c in enumerate(course):
      order = "".join(sorted(order))
      com = list(combinations(order, c))
      arr[i].extend(com)

  for ar in arr:
    cnt = Counter(ar)
    # print(cnt)
    if len(cnt.values()) > 0:
      max_value = max(cnt.values())
      for c in cnt:
        if cnt[c] == max_value and cnt[c] >= 2:
          answer.append("".join(list(c)))

  answer.sort()
  return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))