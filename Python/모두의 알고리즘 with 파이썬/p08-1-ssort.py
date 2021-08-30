def find_min_idx(v):
  min_idx = 0
  for i in range(1, len(v)):
    if v[i] < v[min_idx]:
      min_idx = i
  return min_idx

def sel_sort(v):
  result = []
  while v:  # 주어진 리스트에 값이 남아 있으면 실행
    min_idx = find_min_idx(v) # 리스트에 남아있는 값 중 최솟값의 위치
    value = v.pop(min_idx)  # 찾은 최솟값을 빼내어 value에 저장
    result.append(value)
  return result

v = [2, 4, 5, 1, 3]
print(sel_sort(v))