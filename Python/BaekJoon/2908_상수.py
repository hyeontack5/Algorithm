# 방법 1
a, b = input().split()

a_reverse = ''
b_reverse = ''

for ch in a:
  a_reverse = ch + a_reverse

for ch in b:
  b_reverse = ch + b_reverse

a_reverse = int(a_reverse)
b_reverse = int(b_reverse)

if (a_reverse >= b_reverse):
  print(a_reverse)
else:
  print(b_reverse)
