def solution(s):
    answer = ''
    pos = 0
    
    if (len(s) % 2 != 0):   # s의 길이가 홀수인 경우
        pos = (len(s)//2)  # s의 중앙 위치
        answer += s[pos]
    else:   # s의 길이가 짝수인 경우
        pos = (len(s)//2)
        answer += s[pos-1:pos+1]
    
    return answer