# 방법 1 - 재귀
n = int(input())

def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n-1)

print(factorial(n))

# 방법 2 - math 라이브러리
import math

n = int(input())

print(math.factorial(n))
