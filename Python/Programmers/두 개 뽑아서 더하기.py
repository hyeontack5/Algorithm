def solution(numbers):
    answer = []
    s = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            s.add(numbers[i] + numbers[j])
        
    answer = list(s)
    answer.sort()
    return answer