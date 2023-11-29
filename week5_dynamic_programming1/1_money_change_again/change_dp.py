import math

mon = int(input())
denom = [1, 3, 4]
minCoins = [0] + [math.inf]*mon

for i in range(1, mon+1):
    for j in denom:
        if i>=j:
            coins = minCoins[i-j]+1
            if coins < minCoins[i]:
                minCoins[i] = coins

print(minCoins[mon])