# 방법 1
N = int(input())

for i in range(1, N+1):
  for j in range(0, i):
    print("*", end="")
  print()

# 방법 2
# N = int(input())

# for i in range(1, N+1):
#   print("*" * i)