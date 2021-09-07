a, b = map(int, input().split())

a = bool(a)
b = bool(b)

print((a and (not b)) or ((not a) and b))

# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산