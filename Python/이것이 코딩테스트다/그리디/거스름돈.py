n = int(input())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)
