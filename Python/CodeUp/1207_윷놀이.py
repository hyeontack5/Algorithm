# 방법 1
yut = list(map(int, input().split()))

cnt = 0

for i in range(0, len(yut)):
  if(yut[i] == 1):
    cnt += 1

if (cnt == 1):
  print('도')
elif (cnt == 2):
  print('개')
elif (cnt == 3):
  print('걸')
elif (cnt == 4):
  print('윷')
else:
  print('모')

# 방법 2
# a, b, c, d = map(int, input().split())

# cnt = a + b + c + d

# if (cnt == 4):
#   print('윷')
# elif (cnt == 3):
#   print('걸')
# elif (cnt == 2):
#   print('개')
# elif (cnt == 1):
#   print('도')
# else:
#   print('모')