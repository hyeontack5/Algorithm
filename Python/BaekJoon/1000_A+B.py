# 방법 1
A, B = map(int, input().split())

print(A + B)

# 방법 2
# A, B = input().split()  
# # 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 num1, num2 변수에 저장

# print(int(A) + int(B))	
# # int() 함수로 num1와 num2를 정수로 변환 하고 두수의 합을 출력

# python의 경우 input으로 입력 받을 때 default를 문자로 인식합니다.