# 방법 1
a, b, c = map(int, input().split())

print(min(a, b, c))

# 방법 2
# a, b, c = map(int, input().split())

# result = (a if (a < b) else b) if ((a if (a < b) else b) < c) else c

# print(result)