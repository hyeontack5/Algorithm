menu = [400, 340, 170, 100, 70]

num1, num2 = map(int, input().split())

calorie = menu[num1 - 1] + menu[num2 - 1]

if (calorie > 500):
  print('angry')
else:
  print('no angry')