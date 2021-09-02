T = int(input())

for i in range(1, T+1):
  num1, num2 = map(int, input().split())
  sum = num1 + num2

  print("Case #%d: %d" %(i, sum))

  # print("Case #%s: %s"%(i, sum))
  # %s로 문자열로 바꿔서 출력하는 코드들이 있던데 왜 그런지 모르겠습니다.