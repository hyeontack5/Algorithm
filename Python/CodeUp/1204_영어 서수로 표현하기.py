# 방법 1
n = int(input())

ordinal_n = ''

if(n % 10 == 1):
  ordinal_n = str(n) + 'st'
  if(n == 11):
    ordinal_n = str(n) + 'th'
elif(n % 10 == 2):
  ordinal_n = str(n) + 'nd'
  if(n == 12):
    ordinal_n = str(n) + 'th'
elif(n % 10 == 3):
  ordinal_n = str(n) + 'rd'
  if(n == 13):
    ordinal_n = str(n) + 'th'
else:
  ordinal_n = str(n) + 'th'

print(ordinal_n)

# 방법 2
# n = int(input())

# if(n == 11 or n == 12 or n == 13):
#   print(str(n) + 'th')
# elif(n % 10 == 1):
#   print(str(n) + 'st')
# elif(n % 10 == 2):
#   print(str(n) + 'nd')
# elif(n % 10 == 3):
#   print(str(n) + 'rd')
# else:
#   print(str(n) + 'th')