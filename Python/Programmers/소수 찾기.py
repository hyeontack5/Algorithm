def solution(n):
    num_set = set(range(2, n+1)) # 2부터 n까지의 숫자 배열 만들기

    for i in range(2, n+1):
        if i in num_set: # 배수 제거
            num_set -= set(range(i*2, n+1, i))

    answer = len(num_set)

    return answer