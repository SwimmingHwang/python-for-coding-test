n = input()
l = len(n)
l /= 2
l = int(l)
a = n[:l]
b = n[l:]

a = list(map(int,a))
b = list(map(int,b))

if sum(a) == sum(b):
    print("LUCKY")
else:
    print("READY")






