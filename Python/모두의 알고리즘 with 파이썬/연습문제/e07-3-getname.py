def get_name(stu_no, stu_name, find_num):
  for i in range(0, len(stu_no)):
    if find_num == stu_no[i]:
      return stu_name[i]
  
  return "?"

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "john", "Mike", "Summer"]

find_num = int(input())
print(get_name(stu_no, stu_name, find_num))