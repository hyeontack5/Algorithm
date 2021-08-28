def search_list(v, num):
  result = [] # 새 리스트를 만들어 결괏값을 저장
  for i in range(0, len(v)-1):
    if num == v[i]:
      result.append(i)

  return result

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))