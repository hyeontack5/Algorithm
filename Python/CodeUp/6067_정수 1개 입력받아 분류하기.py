num = int(input())

if (num < 0):
  if(num % 2 == 0):
    print("A")  # 음수이면서 짝수
  else:
    print("B")  # 음수이면서 홀수
else:
  if(num % 2 == 0):
    print("C")  # 양수이면서 짝수
  else:
    print("D")  # 양수이면서 홀수