# 방법 1
n, m = map(int, input().split())

for i in range(0, m):
  for j in range(0, n):
    print("*", end="")
  print()

# 방법 2
# n, m = map(int, input().split())
# answer = ('*' * n + '\n') * m

# print(answer)