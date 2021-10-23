n = int(input())
numbers = list(map(int, input().split()))
max_number = 0

for number in numbers:
  if (number > max_number):
    max_number = number

print(max_number)