# while True:
#   A, B = map(int, input().split())

#   print(A + B)

# 이렇게하면 런타임 에러 (EOFError)가 발생합니다.
# 그 이유는 아무 입력이 없음에도 input().split()으로 A, B에 넣어주려고 하기 때문에 오류가 발생하는 것입니다.

while True:
  try:
    A, B = map(int, input().split())
    print(A+B)
  except:
    break

# 이렇게 작성하면 런타임 에러 문제를 해결할 수 있습니다.