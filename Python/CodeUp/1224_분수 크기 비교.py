# 방법 1
a, b, c, d = map(int, input().split())

if ((a / b) > (c /d)):
  print('>')
elif ((a / b) < (c /d)):
  print('<')
else:
  print('=')

# 방법 2
# a, b, c, d = map(int, input().split())

# 통분 ==> ad / bd  : cb / db
# if ((a * d) > (c * b)):
#   print('>')
# elif ((a * d) < (c * b)):
#   print('<')
# else:
#   print('=')