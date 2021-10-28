def solution(n):
    answer = 0
    yagsu = []
    
    for i in range(1, n+1):
        if (n % i == 0):
            yagsu.append(i)
        
    answer = sum(yagsu)
    return answer