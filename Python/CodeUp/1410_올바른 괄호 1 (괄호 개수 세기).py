# 방법 1
string = input()

print(string.count('('), string.count(')'))

# 방법 2
# string = input()
# openBracket = 0
# closeBracket = 0

# for i in string:
#   if i == '(':
#     openBracket += 1
#   elif i == ')':
#     closeBracket += 1

# print(openBracket, closeBracket)