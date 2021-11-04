# 방법 1
# pasta = []
# juice = []

# for i in range(3):
#   n = int(input())
#   pasta.append(n)
#   pasta.sort()

# for j in range(2):
#   n = int(input())
#   juice.append(n)
#   juice.sort()

# sum = pasta[0] + juice[0]
# price = sum + (sum * 0.1)

# print(price)

# 방법 2

pasta = []
juice = []

for i in range(3):
  pasta.append(float(input()))

for i in range(2):
  juice.append(float(input()))

result = (min(pasta) + min(juice)) * 1.1

print("%.1f" % result)