# 방법 1

# 현재 점수 n
n = input()
length = len(n)

left_score = 0
right_score = 0

for i in range(length // 2):
    left_score += int(n[i])

for j in range(length // 2, length):
    right_score += int(n[j])
if (left_score == right_score):
    print("LUCKY")
else:
    print("READY")
