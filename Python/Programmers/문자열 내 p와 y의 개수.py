# 방법 1
def solution(s):
    answer = True
    cnt1 = 0
    cnt2 = 0
    
    for i in s:
        if (i=='p' or i=='P'):
            cnt1 += 1
        elif (i=='y' or i=='Y'):
            cnt2 += 1
    
    if (cnt1 == cnt2):  # p의 개수와 y의 개수가 같은 경우
        answer = True
    else:    # p의 개수와 y의 개수가 다른 경우
        answer = False
    
    return answer

# 방법 2
# def solution(s):
#     answer = True
    
#     if (s.lower().count('p') == s.lower().count('y')):
#         answer = True
#     else:
#         answer = False
    
#     return answer