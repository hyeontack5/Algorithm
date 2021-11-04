def f():
  answer = ''

  if (n == 1):
    answer += 'hello'
  
  if (n == 2):
    answer += 'world'

  return answer

n = int(input())
print(f())