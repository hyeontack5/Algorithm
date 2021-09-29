# 방법 1
n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
  if a[i] < min :
    min = a[i]

print(min)

# 방법 2
# n = int(input())
# a = input().split()

# for i in range(n):
#   a[i] = int(a[i])

# print(min(a))