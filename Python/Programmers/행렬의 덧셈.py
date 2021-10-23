arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

answer = [[]]

for row in range(len(arr1)):
  for col in range(len(arr1[0])):
    arr1[row][col] += arr2[row][col]

answer = arr1