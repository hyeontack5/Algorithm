a, b = map(int, input().split())

sum = 0

for i in range(a, b+1):
  if (i % 2 == 0):  # 짝수이면 뺌
    sum -= i
  else: # 홀수이면 더함
    sum += i

print(sum)