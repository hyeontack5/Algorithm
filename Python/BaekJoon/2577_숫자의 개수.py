# 방법 1
A = int(input())
B = int(input())
C = int(input())

mul = list(str(A * B * C))
cnt = 0

for i in range(0, 10):
  for j in range(0, len(mul)):
    if mul[j] == str(i):
      cnt += 1
  print(cnt)
  cnt = 0

# for문을 사용

# 방법 2
# A = int(input())
# B = int(input())
# C = int(input())

# mul = list(str(A * B * C))

# for i in range(0, 10):
#   print(mul.count(str(i)))

# count() 함수를 사용