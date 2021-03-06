# 방법 1
n = input()

left = 0
right = 0

for i in range(len(n) // 2):
    left += int(n[i])
    right += int(n[len(n) - 1 - i])

if (left == right):
    print("LUCKY")
else:
    print("READY")

# 방법 2
n = input()

length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summay += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for j in range(length // 2, length):
    summary -= int(n[j])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if (summary == 0):
    print("LUCKY")
else:
    print("READY")
