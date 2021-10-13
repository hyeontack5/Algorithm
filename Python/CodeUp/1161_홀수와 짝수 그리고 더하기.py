a,b = map(int, input().split())

sum = a + b

if (a % 2 == 0):
    print('짝수+',end='')
else:
    print('홀수+',end='')
if (b % 2 == 0):
    print('짝수=',end='')
else:
    print('홀수=',end='')
if (sum % 2 == 0):
    print('짝수')
else:
    print('홀수')