n = int(input())

result = 1
count = 0

while result <= n:
  result *= 10
  count += 1

print(count)

# 방법 2
# n = int(input())

# print(len(str(n)))