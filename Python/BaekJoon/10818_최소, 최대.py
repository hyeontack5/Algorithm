# 방법 1
N = int(input())
array = list(map(int, input().split()))

print(min(array), max(array))

# 방법 2
# N = int(input())
# array = list(map(int, input().split()))
# array.sort()

# print(array[0], array[-1])

# sort() 함수를 사용하여 오름차순으로 정렬합니다.
# array[0], array[-1] index 처음과 마지막을 출력합니다.
# 오름차순으로 정렬하였기 때문에 최솟값과 최댓값이 됩니다.