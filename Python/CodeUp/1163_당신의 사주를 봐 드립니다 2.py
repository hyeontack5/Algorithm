y, m, d = map(int, input().split())

n = (y + m + d) % 1000
n = n // 100

if(n % 2 == 0):
  print("대박")
else:
  print("그럭저럭")