"""
내 답안 프로세스
0. 입력받은 그래프를 인접리스트 형식으로 바꿔주기
1. 시작이 0인거 찾기 & 방문하지 않아야 함
2. 상하좌우 0인 인접리스트 다 방문 끝나면 count +1
3. 1번으로 돌아가기, 1번 조건에 해당하는 노드가 없으면 끝

- 입력받는거 다시 외우기
- 이차원 배열 초기화 하는 것 외우기
- 그래프가 끊기는 경우가 있음.

- 풀이 시간 초과(30m)

<모범 답안과 비교 분석>
- 세지 않아도 되는 1로 되어있는 부분을 "방문한 지점" 이라고 사고를 했어야 했음. -> visited array가 굳이 필요하지 않음.
- dfs 를 문제에 맞게 스스로 각색해서 구현할 줄 알아야 함.
- 단순하게 이차원 배열(2d-array)로 그래프를 탐색했으면 되었는데 adjcent array를 굳이 만들어가면서 해결함-> 오류 발생률이 높아졌고 구현이 복잡해지는 문제가 생김.

"""
def array2d_to_adj_list(array2d):
    global n, m
    adj_list = []
    for i in range(n):
        for j in range(m):
            li = []
            if i >= 1 and array2d[i][j] == array2d[i - 1][j]:
                li.append((i - 1, j))
            if i + 1 < n and array2d[i][j] == array2d[i + 1][j]:
                li.append((i + 1, j))
            if j >= 1 and array2d[i][j] == array2d[i][j - 1]:
                li.append((i, j - 1))
            if j + 1 < m and array2d[i][j] == array2d[i][j + 1]:
                li.append((i, j + 1))
            adj_list.append(li)
    return adj_list

def dfs(graph, v, visited):
    # v 는 ( a,b ) 튜플
    global count
    global m
    # 현재 노드 방문 처리
    visited[v[0]][v[1]] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v[0]*m+v[1]]:
        if not visited[i[0]][i[1]]:
            dfs(graph, (i[0],i[1]), visited)

# Data input
n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(input())

visited = [[0] * m for _ in range(n)]

# 입력받은 2-d array adj-list로 바꿔주기
graph = array2d_to_adj_list(mat)

count = 0
for idx, g in enumerate(graph):
    # 방문하지 않고 값이 0이면 dfs & 갯수 카운트
    if not visited[idx//m][idx%m] and mat[idx//m][idx%m] == '0':
        dfs(graph,(idx//m,idx%m) , visited)
        count += 1
print('cnt=',count)


'''
input 1
4 5
00110
00011
11111
00000
output 3
'''
'''
input 2
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
output 8
'''

"""
모범 답안

"""

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력