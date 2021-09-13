# 방법 1
month = int(input()) 

if (month // 3 == 1): 
  print("spring") 
elif (month // 3 == 2): 
  print("summer") 
elif (month //3 == 3): 
  print("fall") 
else: 
  print("winter")

# 방법 2
# month = int(input())
# season = ''

# if (month in [12, 1, 2]):
#   season = 'winter'
# elif (month in [3, 4, 5]):
#   season = 'spring'
# elif (month in [6, 7, 8]):
#   season = 'summer'
# else:
#   season = 'fall'

# print(season)