# 방법 1
def solution(n):
    answer = 0
    
    numbers = list(str(n))  # integer -> string -> list로 자료형 변환
    numbers.sort(reverse = True)    # sort()로 오름차순으로 정렬하고 reverse로 내림차순으로 만들어줌
    answer = int("".join(numbers))   # join()을 이용하여 list -> string으로 만들어주고 int()로 자료형 변환을 함
    return answer