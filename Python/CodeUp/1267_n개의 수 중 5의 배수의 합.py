n = int(input())
numbers = list(map(int, input().split()))

sum = 0

for number in numbers:
  if (number % 5 == 0):
    sum += number

print(sum)
