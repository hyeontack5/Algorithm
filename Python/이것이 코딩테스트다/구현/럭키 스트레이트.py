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

# 방법 2

# 현재 점수 n
n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")
