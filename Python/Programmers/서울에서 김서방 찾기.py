# 방법 1
def solution(seoul):
    answer = ''
    
    x = seoul.index('Kim')  # seoul에서 'Kim'의 index 위치를 반환함
    answer = '김서방은 '+str(x)+'에 있다'
    
    return answer

# 방법 2
# def solution(seoul):
#     answer = ''
#     kimIdx = 0

#     for i in range(len(seoul)):
#         if (seoul[i] == 'Kim'):
#             return "김서방은 {}에 있다".format(i)