# 방법 1
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a/b, ".2f"))

# 방법 2
# import sys

# def add(n1, n2):
#   return n1 + n2

# def sub(n1, n2):
#   return n1 - n2

# def mul(n1, n2):
#   return n1 * n2

# def div(n1, n2):
#   return n1 // n2

# def rem(n1, n2):
#   return n1 % n2

# def fdiv(n1, n2):
#   return round(n1/n2, 2)

# a, b = map(int,sys.stdin.readline().split())

# print(add(a, b))
# print(sub(a, b))
# print(mul(a, b))
# print(div(a, b))
# print(rem(a, b))
# print(fdiv(a, b))