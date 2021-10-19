grade, group, number = input().split()
group = int(group)
number = int(number)

if(group < 10):
  group = '0' + str(group)

if(number < 10):
  number = '00' + str(number)
elif(number < 100):
  number = '0' + str(number)

print(grade + str(group) + str(number))