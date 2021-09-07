a, b = map(int, input().split())

print(bool(a) or bool(b))

# or 예약어는 주어진 두 불 값 중에서 하나라도 True 이면 True 로 계산하고, 나머지 경우는 False 로 계산
# OR 연산(boolean OR)