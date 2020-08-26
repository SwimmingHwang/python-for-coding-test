"""
데이터 읽는 다양한 방법들 기술
"""
'''
1. N, M을 공백을 기준으로 구분하여 입력 받기
'''
n, m = map(int, input().split())

'''
2. 공백을 기준으로 리스트 입력 받기
'''
data = list(map(int, input().split()))

'''
3. 2차원 리스트의 그래프 정보 입력 받기
- 띄어쓰기 없이 입력받더라도 map 함수의 파라미터가 iterable(여기서 string)이 들어가기 때문에
  글자 하나하나가 매핑되어 int형으로 변환되는 함수를 거쳐 리스트로 반환된다.
'''
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(n, m)
print(graph)

# input and output
# 3 4
# [[1, 2, 3, 4], [5, 6, 7, 8], [1, 3, 1, 3]]

'''
4. sys 라이브러리를 활용하여 빠르게 입력받기
- 입력데이터가 많은 경우 readline()를 통해 시간초과 피하기
- rstrip() 꼭 호출해줘야 함. 엔터가 줄바꿈 기호로 입력되기 때문에 공백 문자를 제거해줘야 함. 
'''
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
print(input_data)
