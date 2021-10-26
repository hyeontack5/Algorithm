t = int(input())

for _ in range(t): # 테스트 케이스 반복 횟수
  r, s = input().split()
  r = int(r)  # r (str -> int)
  text =''
  for i in s:
    text += (i * r)
  
  print(text)
  