def f(num):
  if (num > 0):
    return 'plus'
  elif (num < 0):
    return 'minus'
  else:
    return 'zero'

n = int(input())
print(f(n))