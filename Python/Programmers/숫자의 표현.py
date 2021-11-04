def solution(n):
    answer = 0
    cnt = 0
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            answer += j
            
            if (answer == n):
                answer = 0
                cnt += 1
                break
            if (answer > n):
                answer = 0
                break
            
    answer = cnt
    
    return answer