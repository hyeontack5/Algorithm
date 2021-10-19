# 방법 1
time, score = map(int, input().split())

for i in range(time, 90, 5):
  if(i < 90):
    score += 1

print(score)

# 방법 2
# time, score = map(int, input().split())

# cnt = (90 - time) // 5
# rest = (90 - time) % 5

# score = score + cnt

# if(rest != 0):
#   score += 1

# print(score)