'''
https://www.acmicpc.net/problem/10825
'''
import sys

input = sys.stdin.readline
n = int(input())
info = []

for _ in range(n):
    info.append(list(input().split()))

'''
모범답안 lambda 함수 사용하기
info.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

'''

def setting(data):
    return -int(data[1]), int(data[2]), -int(data[3]), data[0]


info.sort(key=setting, reverse=False)

for i in info:
    print(i[0])

'''
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''
