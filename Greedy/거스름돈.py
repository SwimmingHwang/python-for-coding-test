N = 1260

cnt = 0

for coin in [500,100,50,10]:
    cnt += N // coin
    N %= coin
if N == 0:
    print(cnt)