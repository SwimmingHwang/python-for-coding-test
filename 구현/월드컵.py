'''
5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4

Match array 만들어서
int t1 = match[rount][0]
int t2 = match[rount][1]

'''

arr = [list(map(int, input().split())) for _ in range(4)]

for li in arr:

  a = [li[i:i + 3] for i in range(0, len(li), 3)] # 리스트 컴프리헨션으로 원하는 크기로 array split
  a.sort(key=lambda x: x[1]) # sort 기준 lambda 함수 사


