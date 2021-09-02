# 방법 1
N = int(input())

for i in range(N, 0, -1):
  print(i)

# range([start], stop, [step]) 
# start, step은 생략가능합니다. stop은 생략 불가능합니다.
# start, step을 생략하면 각각 0, 1이 default가 됩니다.

# 방법 2
# N = int(input())

# for i in reversed(range(N)):
#   print(i + 1)

# range()는 순차적인 숫자를 가지는 리스트를 생성하는 함수입니다.
# reversed()는 리스트의 원소를 거꾸로 뒤집고 이를 반환하는 함수입니다.