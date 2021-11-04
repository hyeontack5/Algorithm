def f(num):
  cnt = 0

  for i in range(1, num+1):
    if (num % i == 0):
      cnt += 1
  
  if (cnt == 2):
    return 'prime'
  else:
    return 'composite'

n = int(input())
print(f(n))