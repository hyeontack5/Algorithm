# 방법 1
age = int(input())

ymd = 2012 - age + 1

if(ymd < 2000):
  ymd %= 100
  print(ymd, 1)
else:
  ymd %= 100
  print(ymd, 3)

# 방법 2
# age = int(input())

# ymd = 2012 - age + 1

# if(ymd < 2000):
#   ymd = str(ymd)
#   print(int(ymd[2:4], 1))
# else:
#   ymd = str(ymd)
#   print(int(ymd[2:4], 3))