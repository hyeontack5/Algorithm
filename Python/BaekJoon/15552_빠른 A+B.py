import sys  # sys 모듈 읽기

T = int(sys.stdin.readline())

for i in range(0, T):
  num1, num2 = map(int, sys.stdin.readline().split())

  print(num1 + num2)

  # sys.stdin.readline() 함수는 사용 방식과 기능은 input 함수를 사용할 때와 동일합니다.