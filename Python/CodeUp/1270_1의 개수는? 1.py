n = int(input())

count = 0

for i in range(1, n+1):
  if (i % 10 == 1):
    count += 1

print(count)