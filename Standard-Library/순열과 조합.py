"""
itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
permutations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산
combinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산
"""

data = ['A', 'B', 'C']

# permutations
# n!/(n-r)!
from itertools import permutations

result = list(permutations(data, r=3))
print(result)  # 3 X 2 X 1 =
'''
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
'''

# combinations
# n!/(n-r)!r!
from itertools import combinations

result = list(combinations(data, r=2))
print(result)  # 3 X 2 X 1 / 2
'''
[('A', 'B'), ('A', 'C'), ('B', 'C')]
'''

# 중복 허용 permutations
# n^r
from itertools import product

result = list(product(data, repeat=2))
print(result)  # 3 X 3  9개 출력
'''
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
'''

# 중복 허용 combinations
# n+1-r C r
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, r=2))
print(result)
'''
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
'''
