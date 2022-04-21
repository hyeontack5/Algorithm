# 방법 1
num_list = []
max_num = 0

for i in range(9):
  num_list.append(int(input()))

for j in range(0, len(num_list)):
  if num_list[j] > max_num:
    max_num = num_list[j]
    max_index = j + 1

print(max_num, max_index, sep='\n')

# for 루프를 사용하여 최댓값 찾기

# 방법 2
# num_list = []

# for i in range(9):
#   num_list.append(int(input()))

# print(max(num_list))
# print(num_list.index(max(num_list))+1)

# max() 함수를 사용하여 최댓값 찾기