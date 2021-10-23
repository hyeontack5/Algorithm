# 방법 1
n = int(input())

count = 0

for i in range(2, n+1):
  if (n % i == 0):
    count += 1

if (count == 1):
  print('prime')
else:
  print('not prime')

# 방법 2
# n = int(input())

# now = 'prime'

# for i in range(2, n):
#   if (n % i == 0):
#     now = 'not prime'
#     break

# print(now)