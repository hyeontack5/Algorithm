# 방법 1
a, b = map(int, input().split())

temp = 0
temp = a
a = b
b = temp

print(a, b)

# 방법 2
# a, b = map(int, input().split())

# print(b, a)