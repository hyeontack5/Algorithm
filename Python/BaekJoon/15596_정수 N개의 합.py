# 방법 1
# def solve(a):
#   return sum(a) # sum()함수를 이용한 경우

# 방법 2
def solve(a):
  total = 0

  for i in a: # for문을 이용한 경우
    total += i

  return total