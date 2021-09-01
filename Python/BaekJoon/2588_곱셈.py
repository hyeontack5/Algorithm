# 방법 1
num1 = int(input())
num2 = int(input())

print(num1*(num2%10), num1*((num2//10)%10), num1*(num2//100), num1*num2, sep='\n')

# 방법 2
# num1 = int(input())
# num2 = input()  
# # input()은 default로 문자열로 저장됩니다.
# # input() = str(input())

# print(num1 * int(num2[2]))
# print(num1 * int(num2[1]))
# print(num1 * int(num2[0]))
# print(num1 * int(num2))