def solution(left, right):
    answer = 0
    cnt = 0
    
    for i in range(left, right+1):  # left ~ ringt까지의 수
        for j in range(1, i+1):
            if (i % j == 0):    # 약수의 갯수를 카운트 함
                cnt += 1
        if (cnt % 2 == 0):  # 약수의 갯수가 짝수이면 더함
            answer += i
            cnt = 0
        else:   # 약수의 갯수가 홀수이면 뺌
            answer -= i
            cnt = 0
    
    return answer