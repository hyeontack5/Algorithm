# 방법 1
N = int(input())

for i in range(1, N+1):
  for j in range(1, (N-i)+1):
    print(" ", end="")
  for j in range(1, i+1):
    print("*", end="")
  print()

# 방법 2
# N = int(input())

# for i in range(1, N+1):
#   print(" " * (N-i) + "*" * i)