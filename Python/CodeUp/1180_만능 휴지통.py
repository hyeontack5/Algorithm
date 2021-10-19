# 방법 1
n = int(input())

one = n % 10
ten = n // 10

result = one * 10 + ten
result *= 2

if(result > 99):
  result %= 100

print(result)

if(result <= 50):
  print('GOOD')
else:
  print('OH MY GOD')

# 방법 2
# n = input()

# result = n[1] + n[0]
# result = int(result) * 2

# if(result > 99):
#   result %= 100

# print(result)

# if(result <= 50):
#   print('GOOD')
# else:
#   print('OH MY GOD')