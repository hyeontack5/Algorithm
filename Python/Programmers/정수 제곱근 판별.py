def solution(n):
    answer = 0
    
    for x in range(1, n+1):
        if (n == (x**2)):
            answer = ((x+1)**2)
            break
        else:
            answer = -1
    return answer