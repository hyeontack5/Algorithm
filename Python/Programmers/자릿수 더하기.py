def solution(n):
    answer = 0
    
    numbers = list(str(n))
    for i in numbers:
        answer += int(i)

    return answer