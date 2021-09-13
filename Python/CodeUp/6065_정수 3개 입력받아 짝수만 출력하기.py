# 방법 1
a, b, c = map(int, input().split())

if (a % 2 == 0):
  print(a)

if (b % 2 == 0):
  print(b) 

if (c % 2 == 0):
  print(c) 

# 방법 2
# data = input().split()

# for i in data:
#   if(int(i) % 2 == 0):
#     print(int(i))