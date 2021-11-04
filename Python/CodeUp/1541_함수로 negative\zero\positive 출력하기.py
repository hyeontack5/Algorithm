def f(num):
  if (num > 0):
    return 'positive'
  elif (num < 0):
    return 'negative'
  else:
    return 'zero'

n = int(input())
print(f(n))