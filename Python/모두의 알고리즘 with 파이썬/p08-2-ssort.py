def sel_sort(v):
  for i in range(0, len(v) - 1):
    min_idx = i
    for j in range(i + 1, len(v)):
      if v[j] < v[min_idx]:
        min_idx = j
    v[i], v[min_idx] = v[min_idx], v[i]

  return v

v = [2, 4, 5, 1, 3]
print(sel_sort(v))