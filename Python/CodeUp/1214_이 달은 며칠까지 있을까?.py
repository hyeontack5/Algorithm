month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year, month = map(int, input().split())

if (month != 2):
  print(month_list[month - 1])
elif ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)): # 윤년인 경우
  print(month_list[1] + 1)
else: # 윤년이 아닌 경우
  print(month_list[1])