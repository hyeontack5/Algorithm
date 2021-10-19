# 방법 1
ymd, gender = map(int, input().split())
age = 0

ymd = ymd // 10000

if(gender == 1 or gender == 2):
  age = ((2012 - 1900) - ymd) + 1
  print(age)
else:
  age = ((2012 - 2000) - ymd) + 1
  print(age)

# 방법 2
# ymd, gender = map(int, input().split())

# ymd = ymd // 10000

# if(gender <= 2):
#   ymd = ymd + 1900
# else:
#   ymd = ymd + 2000

# print(2012 - ymd + 1)