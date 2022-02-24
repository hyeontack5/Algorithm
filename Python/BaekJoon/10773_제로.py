import sys

# 정수 k 입력
k = int(input())

stack = list()

for i in range(k):
    num = int(sys.stdin.readline())

    # 만약 num이 0이면 가장 최근 입력된 값 제거
    if (num == 0):
        stack.pop(-1)
    else:
        stack.append(num)

print(sum(stack))
