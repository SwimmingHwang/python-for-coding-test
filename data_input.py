# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 그래프 정보 입력 받기
# 띄어쓰기 없이 입력받더라도 map 함수의 파라미터가 iterable(여기서 string)이 들어가기 때문에
# 글자 하나하나가 매핑되어 int형으로 변환되는 함수를 거쳐 리스트로 반환된다.

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(n, m)
print(graph)

'''
3 4
[[1, 2, 3, 4], [5, 6, 7, 8], [1, 3, 1, 3]]
'''