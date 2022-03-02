## python coding test input case

1. 붙어있는 array   
4 5   
00110   
00011   
11111   
00000   

```python
n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]
``` 

2. 공백있는 array   
5 5   
1 2 3 4 5   
5 4 3 2 1   
2 3 4 5 6   
6 5 4 3 2   
1 2 1 2 1   
   

```python
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
```
