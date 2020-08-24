n, k = map(int, input().split())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

a_li.sort()
b_li.sort(reverse=True)

for i in range(k):


    if a_li[i] >= b_li[i]:
        break
    a_li[i] = b_li[i]
print(a_li)
print(sum(a_li))



'''
input
5 3
1 2 5 4 3
5 5 6 6 5
'''