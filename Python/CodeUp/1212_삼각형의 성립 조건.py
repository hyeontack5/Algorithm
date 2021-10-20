# 방법 1
sides = list(map(int, input().split()))

long_side = max(sides)
sum_sides = sum(sides)
short_sides = sum_sides - long_side

if (long_side < short_sides):
  print('yes')
else:
  print('no')
