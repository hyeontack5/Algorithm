# 방법 1
hour, min = map(int, input().split())

if(min < 30):
  if(hour == 0):
    hour += 23
  else:
    hour -= 1
  min = (60 - 30 + min)
else:
  min -= 30

print(hour, min)

# 방법 2
# hour, min = map(int, input().split())

# total = 0
# total = hour * 60 + min
# total = total - 30

# if(total < 0):
#   hour = 23
#   min = 60 + total
# else:
#   hour = total // 60
#   min = total % 60

# print(hour, min)