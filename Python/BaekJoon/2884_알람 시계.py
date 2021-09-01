# 방법 1
hour, min = map(int, input().split())

if min < 45:
  if hour == 0:
    hour = 23
    min += 60
  else:
    hour -= 1
    min += 60

print(hour, min-45)

# 방법 2
# hour, minute = map(int, input().split())

# if minute > 44:
#     print(hour, minute-45)
# elif minute <= 44 and hour >= 1:
#     print(hour-1, minute+15)
# else:
#     print(23, minute+15)